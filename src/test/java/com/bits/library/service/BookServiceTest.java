package com.bits.library.service;

import com.bits.library.entity.Author;
import com.bits.library.entity.Book;
import com.bits.library.repository.BookRepository;
import com.bits.library.service.impl.BookServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class BookServiceTest {

    @Mock
    private BookRepository bookRepository;

    @InjectMocks
    private BookServiceImpl bookService;

    private Author author;
    private Book book1;
    private Book book2;

    @BeforeEach
    void setUp() {
        author = new Author("George", "Orwell", "george.orwell@test.com", 1903, "British");
        author.setId(1L);

        book1 = new Book("1984", "978-0-001", "Dystopian Fiction", 1949, 12.99, author);
        book1.setId(1L);

        book2 = new Book("Animal Farm", "978-0-002", "Political Satire", 1945, 9.99, author);
        book2.setId(2L);
    }

    @Test
    void getAllBooks_ShouldReturnAllBooks() {
        when(bookRepository.findAll()).thenReturn(Arrays.asList(book1, book2));

        List<Book> result = bookService.getAllBooks();

        assertThat(result).hasSize(2);
        assertThat(result).containsExactlyInAnyOrder(book1, book2);
        verify(bookRepository, times(1)).findAll();
    }

    @Test
    void getAllBooks_WhenNoBooks_ShouldReturnEmptyList() {
        when(bookRepository.findAll()).thenReturn(Arrays.asList());

        List<Book> result = bookService.getAllBooks();

        assertThat(result).isEmpty();
        verify(bookRepository, times(1)).findAll();
    }

    @Test
    void saveBook_ShouldSaveAndReturnBook() {
        Book newBook = new Book("New Book", "978-0-999", "Fiction", 2020, 15.99, author);
        Book savedBook = new Book("New Book", "978-0-999", "Fiction", 2020, 15.99, author);
        savedBook.setId(3L);

        when(bookRepository.save(any(Book.class))).thenReturn(savedBook);

        Book result = bookService.saveBook(newBook);

        assertThat(result.getId()).isEqualTo(3L);
        assertThat(result.getTitle()).isEqualTo("New Book");
        verify(bookRepository, times(1)).save(newBook);
    }

    @Test
    void saveBook_ShouldCallRepositorySave() {
        when(bookRepository.save(book1)).thenReturn(book1);

        bookService.saveBook(book1);

        verify(bookRepository).save(book1);
    }

    @Test
    void saveBook_ShouldPersistAllFields() {
        Book book = new Book("Test Title", "978-0-123", "Mystery", 2021, 18.50, author);
        when(bookRepository.save(book)).thenReturn(book);

        Book result = bookService.saveBook(book);

        assertThat(result.getTitle()).isEqualTo("Test Title");
        assertThat(result.getIsbn()).isEqualTo("978-0-123");
        assertThat(result.getGenre()).isEqualTo("Mystery");
        assertThat(result.getPublishedYear()).isEqualTo(2021);
        assertThat(result.getPrice()).isEqualTo(18.50);
        assertThat(result.getAuthor()).isEqualTo(author);
    }

    @Test
    void getBookById_WhenExists_ShouldReturnBook() {
        when(bookRepository.findById(1L)).thenReturn(Optional.of(book1));

        Optional<Book> result = bookService.getBookById(1L);

        assertThat(result).isPresent();
        assertThat(result.get().getTitle()).isEqualTo("1984");
    }

    @Test
    void getBookById_WhenNotExists_ShouldReturnEmpty() {
        when(bookRepository.findById(99L)).thenReturn(Optional.empty());

        Optional<Book> result = bookService.getBookById(99L);

        assertThat(result).isEmpty();
    }

    @Test
    void updateBook_WhenBookExists_ShouldUpdateAndReturn() {
        Book updateDetails = new Book("1984 Updated", "978-0-001", "Dystopian Fiction", 1949, 14.99, author);

        Book updatedBook = new Book("1984 Updated", "978-0-001", "Dystopian Fiction", 1949, 14.99, author);
        updatedBook.setId(1L);

        when(bookRepository.findById(1L)).thenReturn(Optional.of(book1));
        when(bookRepository.save(any(Book.class))).thenReturn(updatedBook);

        Book result = bookService.updateBook(1L, updateDetails);

        assertThat(result.getTitle()).isEqualTo("1984 Updated");
        assertThat(result.getPrice()).isEqualTo(14.99);
        verify(bookRepository).findById(1L);
        verify(bookRepository).save(any(Book.class));
    }

    @Test
    void updateBook_WhenBookNotFound_ShouldThrowException() {
        Book updateDetails = new Book("Ghost Book", "978-0-000", "Unknown", 2020, 5.99, author);

        when(bookRepository.findById(99L)).thenReturn(Optional.empty());

        assertThatThrownBy(() -> bookService.updateBook(99L, updateDetails))
                .isInstanceOf(RuntimeException.class)
                .hasMessageContaining("Book not found with id: 99");

        verify(bookRepository).findById(99L);
        verify(bookRepository, never()).save(any());
    }

    @Test
    void deleteBook_ShouldCallRepositoryDeleteById() {
        doNothing().when(bookRepository).deleteById(1L);

        bookService.deleteBook(1L);

        verify(bookRepository, times(1)).deleteById(1L);
    }

    @Test
    void findByGenre_ShouldReturnMatchingBooks() {
        when(bookRepository.findByGenre("Dystopian Fiction")).thenReturn(Arrays.asList(book1));

        List<Book> result = bookService.findByGenre("Dystopian Fiction");

        assertThat(result).hasSize(1);
        assertThat(result.get(0).getTitle()).isEqualTo("1984");
        verify(bookRepository).findByGenre("Dystopian Fiction");
    }

    @Test
    void findByGenre_WhenNoMatch_ShouldReturnEmptyList() {
        when(bookRepository.findByGenre("Fantasy")).thenReturn(Arrays.asList());

        List<Book> result = bookService.findByGenre("Fantasy");

        assertThat(result).isEmpty();
    }

    @Test
    void findByAuthorNationality_ShouldReturnMatchingBooks() {
        when(bookRepository.findByAuthorNationality("British")).thenReturn(Arrays.asList(book1, book2));

        List<Book> result = bookService.findByAuthorNationality("British");

        assertThat(result).hasSize(2);
        verify(bookRepository).findByAuthorNationality("British");
    }

    @Test
    void findByAuthorId_ShouldReturnBooksForAuthor() {
        when(bookRepository.findByAuthorId(1L)).thenReturn(Arrays.asList(book1, book2));

        List<Book> result = bookService.findByAuthorId(1L);

        assertThat(result).hasSize(2);
        verify(bookRepository).findByAuthorId(1L);
    }
}
