package com.bits.library.controller;

import com.bits.library.entity.Author;
import com.bits.library.entity.Book;
import com.bits.library.service.AuthorService;
import com.bits.library.service.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.List;
import java.util.Optional;

@Controller
@RequestMapping("/books")
public class BookController {

    private final BookService bookService;
    private final AuthorService authorService;

    @Autowired
    public BookController(BookService bookService, AuthorService authorService) {
        this.bookService = bookService;
        this.authorService = authorService;
    }

    @GetMapping
    public String listBooks(Model model) {
        List<Book> books = bookService.getAllBooks();
        model.addAttribute("books", books);
        model.addAttribute("pageTitle", "Books");
        return "books/list";
    }

    @GetMapping("/new")
    public String showAddForm(Model model) {
        model.addAttribute("book", new Book());
        model.addAttribute("authors", authorService.getAllAuthors());
        model.addAttribute("pageTitle", "Add New Book");
        model.addAttribute("formAction", "/books/save");
        model.addAttribute("isEdit", false);
        return "books/form";
    }

    @PostMapping("/save")
    public String saveBook(@RequestParam String title,
                            @RequestParam String isbn,
                            @RequestParam String genre,
                            @RequestParam int publishedYear,
                            @RequestParam double price,
                            @RequestParam Long authorId,
                            RedirectAttributes redirectAttributes) {
        try {
            Optional<Author> authorOpt = authorService.getAuthorById(authorId);
            if (!authorOpt.isPresent()) {
                redirectAttributes.addFlashAttribute("errorMessage", "Selected author not found.");
                return "redirect:/books/new";
            }
            Book book = new Book(title, isbn, genre, publishedYear, price, authorOpt.get());
            bookService.saveBook(book);
            redirectAttributes.addFlashAttribute("successMessage", "Book added successfully!");
        } catch (DataIntegrityViolationException e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error: A book with this ISBN already exists.");
            return "redirect:/books/new";
        } catch (Exception e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error saving book: " + e.getMessage());
            return "redirect:/books/new";
        }
        return "redirect:/books";
    }

    @GetMapping("/edit/{id}")
    public String showEditForm(@PathVariable Long id, Model model,
                                RedirectAttributes redirectAttributes) {
        Optional<Book> bookOpt = bookService.getBookById(id);
        if (!bookOpt.isPresent()) {
            redirectAttributes.addFlashAttribute("errorMessage", "Book not found with id: " + id);
            return "redirect:/books";
        }
        model.addAttribute("book", bookOpt.get());
        model.addAttribute("authors", authorService.getAllAuthors());
        model.addAttribute("pageTitle", "Edit Book");
        model.addAttribute("formAction", "/books/update/" + id);
        model.addAttribute("isEdit", true);
        return "books/form";
    }

    @PostMapping("/update/{id}")
    public String updateBook(@PathVariable Long id,
                              @RequestParam String title,
                              @RequestParam String isbn,
                              @RequestParam String genre,
                              @RequestParam int publishedYear,
                              @RequestParam double price,
                              @RequestParam Long authorId,
                              RedirectAttributes redirectAttributes) {
        try {
            Optional<Author> authorOpt = authorService.getAuthorById(authorId);
            if (!authorOpt.isPresent()) {
                redirectAttributes.addFlashAttribute("errorMessage", "Selected author not found.");
                return "redirect:/books/edit/" + id;
            }
            Book bookDetails = new Book(title, isbn, genre, publishedYear, price, authorOpt.get());
            bookService.updateBook(id, bookDetails);
            redirectAttributes.addFlashAttribute("successMessage", "Book updated successfully!");
        } catch (DataIntegrityViolationException e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error: A book with this ISBN already exists.");
            return "redirect:/books/edit/" + id;
        } catch (Exception e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error updating book: " + e.getMessage());
            return "redirect:/books/edit/" + id;
        }
        return "redirect:/books";
    }

    @GetMapping("/delete/{id}")
    public String deleteBook(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        try {
            bookService.deleteBook(id);
            redirectAttributes.addFlashAttribute("successMessage", "Book deleted successfully!");
        } catch (Exception e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error deleting book: " + e.getMessage());
        }
        return "redirect:/books";
    }

    @GetMapping("/byNationality")
    public String booksByNationality(@RequestParam(required = false) String nationality, Model model) {
        model.addAttribute("pageTitle", "Books by Author Nationality");
        model.addAttribute("nationality", nationality);
        if (nationality != null && !nationality.trim().isEmpty()) {
            List<Book> books = bookService.findByAuthorNationality(nationality.trim());
            model.addAttribute("books", books);
        }
        return "books/byNationality";
    }
}
