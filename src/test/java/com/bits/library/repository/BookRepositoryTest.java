package com.bits.library.repository;

import com.bits.library.entity.Author;
import com.bits.library.entity.Book;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
public class BookRepositoryTest {

    @Autowired
    private TestEntityManager entityManager;

    @Autowired
    private BookRepository bookRepository;

    private Author britishAuthor;
    private Author americanAuthor;
    private Author russianAuthor;

    private Book book1;
    private Book book2;
    private Book book3;
    private Book book4;

    @BeforeEach
    void setUp() {
        britishAuthor = new Author("George", "Orwell", "george.orwell@test.com", 1903, "British");
        americanAuthor = new Author("Ernest", "Hemingway", "ernest.hemingway@test.com", 1899, "American");
        russianAuthor = new Author("Leo", "Tolstoy", "leo.tolstoy@test.com", 1828, "Russian");

        entityManager.persist(britishAuthor);
        entityManager.persist(americanAuthor);
        entityManager.persist(russianAuthor);

        book1 = new Book("1984", "978-0-001", "Dystopian Fiction", 1949, 12.99, britishAuthor);
        book2 = new Book("Animal Farm", "978-0-002", "Political Satire", 1945, 9.99, britishAuthor);
        book3 = new Book("The Old Man and the Sea", "978-0-003", "Literary Fiction", 1952, 11.99, americanAuthor);
        book4 = new Book("War and Peace", "978-0-004", "Historical Fiction", 1869, 19.99, russianAuthor);

        entityManager.persist(book1);
        entityManager.persist(book2);
        entityManager.persist(book3);
        entityManager.persist(book4);
        entityManager.flush();
    }

    @Test
    void findByGenre_WhenGenreExists_ShouldReturnBooks() {
        List<Book> dysBooks = bookRepository.findByGenre("Dystopian Fiction");

        assertThat(dysBooks).hasSize(1);
        assertThat(dysBooks.get(0).getTitle()).isEqualTo("1984");
    }

    @Test
    void findByGenre_WhenGenreDoesNotExist_ShouldReturnEmpty() {
        List<Book> fantasyBooks = bookRepository.findByGenre("Fantasy");

        assertThat(fantasyBooks).isEmpty();
    }

    @Test
    void findByGenre_WhenMultipleBooksHaveSameGenre_ShouldReturnAll() {
        Book book5 = new Book("Another Fiction", "978-0-005", "Literary Fiction", 2000, 8.99, americanAuthor);
        entityManager.persist(book5);
        entityManager.flush();

        List<Book> litFictionBooks = bookRepository.findByGenre("Literary Fiction");

        assertThat(litFictionBooks).hasSize(2);
    }

    @Test
    void findByAuthorNationality_WhenNationalityExists_ShouldReturnBooks() {
        List<Book> britishBooks = bookRepository.findByAuthorNationality("British");

        assertThat(britishBooks).hasSize(2);
        assertThat(britishBooks).extracting(Book::getTitle)
                .containsExactlyInAnyOrder("1984", "Animal Farm");
    }

    @Test
    void findByAuthorNationality_WhenNationalityHasOneBook_ShouldReturnOneBook() {
        List<Book> russianBooks = bookRepository.findByAuthorNationality("Russian");

        assertThat(russianBooks).hasSize(1);
        assertThat(russianBooks.get(0).getTitle()).isEqualTo("War and Peace");
    }

    @Test
    void findByAuthorNationality_WhenNationalityDoesNotExist_ShouldReturnEmpty() {
        List<Book> japaneseBooks = bookRepository.findByAuthorNationality("Japanese");

        assertThat(japaneseBooks).isEmpty();
    }

    @Test
    void findByAuthorNationality_ShouldReturnBooksWithAuthorInfo() {
        List<Book> americanBooks = bookRepository.findByAuthorNationality("American");

        assertThat(americanBooks).hasSize(1);
        assertThat(americanBooks.get(0).getAuthor().getNationality()).isEqualTo("American");
        assertThat(americanBooks.get(0).getAuthor().getLastName()).isEqualTo("Hemingway");
    }

    @Test
    void findByAuthorId_ShouldReturnBooksForAuthor() {
        List<Book> books = bookRepository.findByAuthorId(britishAuthor.getId());

        assertThat(books).hasSize(2);
    }

    @Test
    void findByAuthorId_WhenAuthorHasNoBooks_ShouldReturnEmpty() {
        Author newAuthor = new Author("Franz", "Kafka", "kafka@test.com", 1883, "Czech");
        entityManager.persist(newAuthor);
        entityManager.flush();

        List<Book> books = bookRepository.findByAuthorId(newAuthor.getId());

        assertThat(books).isEmpty();
    }

    @Test
    void save_ShouldPersistBook() {
        Book newBook = new Book("New Title", "978-0-999", "Thriller", 2020, 15.99, americanAuthor);
        Book saved = bookRepository.save(newBook);

        assertThat(saved.getId()).isNotNull();
        assertThat(saved.getIsbn()).isEqualTo("978-0-999");
    }

    @Test
    void findAll_ShouldReturnAllBooks() {
        List<Book> all = bookRepository.findAll();

        assertThat(all).hasSize(4);
    }
}
