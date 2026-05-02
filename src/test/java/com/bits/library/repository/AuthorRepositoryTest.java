package com.bits.library.repository;

import com.bits.library.entity.Author;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
public class AuthorRepositoryTest {

    @Autowired
    private TestEntityManager entityManager;

    @Autowired
    private AuthorRepository authorRepository;

    private Author author1;
    private Author author2;
    private Author author3;

    @BeforeEach
    void setUp() {
        author1 = new Author("George", "Orwell", "george.orwell@test.com", 1903, "British");
        author2 = new Author("J.K.", "Rowling", "jk.rowling@test.com", 1965, "British");
        author3 = new Author("Ernest", "Hemingway", "ernest.hemingway@test.com", 1899, "American");

        entityManager.persist(author1);
        entityManager.persist(author2);
        entityManager.persist(author3);
        entityManager.flush();
    }

    @Test
    void findByEmail_WhenEmailExists_ShouldReturnAuthor() {
        Optional<Author> found = authorRepository.findByEmail("george.orwell@test.com");

        assertThat(found).isPresent();
        assertThat(found.get().getFirstName()).isEqualTo("George");
        assertThat(found.get().getLastName()).isEqualTo("Orwell");
    }

    @Test
    void findByEmail_WhenEmailDoesNotExist_ShouldReturnEmpty() {
        Optional<Author> found = authorRepository.findByEmail("nonexistent@test.com");

        assertThat(found).isEmpty();
    }

    @Test
    void findByEmail_ShouldBeCaseSpecific() {
        Optional<Author> found = authorRepository.findByEmail("GEORGE.ORWELL@TEST.COM");
        assertThat(found).isEmpty();
    }

    @Test
    void findByNationality_WhenNationalityExists_ShouldReturnMatchingAuthors() {
        List<Author> britishAuthors = authorRepository.findByNationality("British");

        assertThat(britishAuthors).hasSize(2);
        assertThat(britishAuthors).extracting(Author::getLastName)
                .containsExactlyInAnyOrder("Orwell", "Rowling");
    }

    @Test
    void findByNationality_WhenNationalityExistsForOneAuthor_ShouldReturnOneAuthor() {
        List<Author> americanAuthors = authorRepository.findByNationality("American");

        assertThat(americanAuthors).hasSize(1);
        assertThat(americanAuthors.get(0).getFirstName()).isEqualTo("Ernest");
    }

    @Test
    void findByNationality_WhenNationalityDoesNotExist_ShouldReturnEmptyList() {
        List<Author> russianAuthors = authorRepository.findByNationality("Russian");

        assertThat(russianAuthors).isEmpty();
    }

    @Test
    void save_ShouldPersistAuthor() {
        Author newAuthor = new Author("Mark", "Twain", "mark.twain@test.com", 1835, "American");
        Author saved = authorRepository.save(newAuthor);

        assertThat(saved.getId()).isNotNull();
        assertThat(saved.getFirstName()).isEqualTo("Mark");
    }

    @Test
    void findAll_ShouldReturnAllAuthors() {
        List<Author> all = authorRepository.findAll();

        assertThat(all).hasSize(3);
    }

    @Test
    void findById_WhenExists_ShouldReturnAuthor() {
        Optional<Author> found = authorRepository.findById(author1.getId());

        assertThat(found).isPresent();
        assertThat(found.get().getEmail()).isEqualTo("george.orwell@test.com");
    }

    @Test
    void delete_ShouldRemoveAuthor() {
        authorRepository.delete(author3);

        Optional<Author> found = authorRepository.findById(author3.getId());
        assertThat(found).isEmpty();
    }
}
