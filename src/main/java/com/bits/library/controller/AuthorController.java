package com.bits.library.controller;

import com.bits.library.entity.Author;
import com.bits.library.service.AuthorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.util.List;
import java.util.Optional;

@Controller
@RequestMapping("/authors")
public class AuthorController {

    private final AuthorService authorService;

    @Autowired
    public AuthorController(AuthorService authorService) {
        this.authorService = authorService;
    }

    @GetMapping
    public String listAuthors(Model model) {
        List<Author> authors = authorService.getAllAuthors();
        model.addAttribute("authors", authors);
        model.addAttribute("pageTitle", "Authors");
        return "authors/list";
    }

    @GetMapping("/new")
    public String showAddForm(Model model) {
        model.addAttribute("author", new Author());
        model.addAttribute("pageTitle", "Add New Author");
        model.addAttribute("formAction", "/authors/save");
        model.addAttribute("isEdit", false);
        return "authors/form";
    }

    @PostMapping("/save")
    public String saveAuthor(@ModelAttribute Author author,
                              RedirectAttributes redirectAttributes) {
        try {
            authorService.saveAuthor(author);
            redirectAttributes.addFlashAttribute("successMessage", "Author added successfully!");
        } catch (DataIntegrityViolationException e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error: An author with this email already exists.");
            return "redirect:/authors/new";
        } catch (Exception e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error saving author: " + e.getMessage());
            return "redirect:/authors/new";
        }
        return "redirect:/authors";
    }

    @GetMapping("/edit/{id}")
    public String showEditForm(@PathVariable Long id, Model model,
                                RedirectAttributes redirectAttributes) {
        Optional<Author> authorOpt = authorService.getAuthorById(id);
        if (!authorOpt.isPresent()) {
            redirectAttributes.addFlashAttribute("errorMessage", "Author not found with id: " + id);
            return "redirect:/authors";
        }
        model.addAttribute("author", authorOpt.get());
        model.addAttribute("pageTitle", "Edit Author");
        model.addAttribute("formAction", "/authors/update/" + id);
        model.addAttribute("isEdit", true);
        return "authors/form";
    }

    @PostMapping("/update/{id}")
    public String updateAuthor(@PathVariable Long id,
                                @ModelAttribute Author author,
                                RedirectAttributes redirectAttributes) {
        try {
            authorService.updateAuthor(id, author);
            redirectAttributes.addFlashAttribute("successMessage", "Author updated successfully!");
        } catch (DataIntegrityViolationException e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error: An author with this email already exists.");
            return "redirect:/authors/edit/" + id;
        } catch (Exception e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error updating author: " + e.getMessage());
            return "redirect:/authors/edit/" + id;
        }
        return "redirect:/authors";
    }

    @GetMapping("/delete/{id}")
    public String deleteAuthor(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        try {
            authorService.deleteAuthor(id);
            redirectAttributes.addFlashAttribute("successMessage", "Author deleted successfully!");
        } catch (Exception e) {
            redirectAttributes.addFlashAttribute("errorMessage",
                    "Error deleting author: " + e.getMessage());
        }
        return "redirect:/authors";
    }
}
