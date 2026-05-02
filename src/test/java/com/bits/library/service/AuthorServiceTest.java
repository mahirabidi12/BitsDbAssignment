package com.bits.library.service;

import com.bits.library.entity.Author;
import com.bits.library.repository.AuthorRepository;
import com.bits.library.service.impl.AuthorServiceImpl;
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
public class AuthorServiceTest {

    @Mock
    private AuthorRepository authorRepository;

    @InjectMocks
    private AuthorServiceImpl authorService;

    private Author author1;
    private Author author2;

    @BeforeEach
    void setUp() {
        author1 = new Author("George", "Orwell", "george.orwell@test.com", 1903, "British");
        author1.setId(1L);

        author2 = new Author("J.K.", "Rowling", "jk.rowling@test.com", 1965, "British");
        author2.setId(2L);
    }

    @Test
    void getAllAuthors_ShouldReturnAllAuthors() {
        when(authorRepository.findAll()).thenReturn(Arrays.asList(author1, author2));

        List<Author> result = authorService.getAllAuthors();

        assertThat(result).hasSize(2);
        assertThat(result).containsExactlyInAnyOrder(author1, author2);
        verify(authorRepository, times(1)).findAll();
    }

    @Test
    void getAllAuthors_WhenNoAuthors_ShouldReturnEmptyList() {
        when(authorRepository.findAll()).thenReturn(Arrays.asList());

        List<Author> result = authorService.getAllAuthors();

        assertThat(result).isEmpty();
        verify(authorRepository, times(1)).findAll();
    }

    @Test
    void saveAuthor_ShouldSaveAndReturnAuthor() {
        Author newAuthor = new Author("Mark", "Twain", "mark.twain@test.com", 1835, "American");
        Author savedAuthor = new Author("Mark", "Twain", "mark.twain@test.com", 1835, "American");
        savedAuthor.setId(3L);

        when(authorRepository.save(any(Author.class))).thenReturn(savedAuthor);

        Author result = authorService.saveAuthor(newAuthor);

        assertThat(result.getId()).isEqualTo(3L);
        assertThat(result.getFirstName()).isEqualTo("Mark");
        verify(authorRepository, times(1)).save(newAuthor);
    }

    @Test
    void saveAuthor_ShouldCallRepositorySave() {
        when(authorRepository.save(author1)).thenReturn(author1);

        authorService.saveAuthor(author1);

        verify(authorRepository).save(author1);
    }

    @Test
    void updateAuthor_WhenAuthorExists_ShouldUpdateAndReturn() {
        Author updateDetails = new Author("George", "Orwell-Updated", "george.new@test.com", 1903, "British");

        Author updatedAuthor = new Author("George", "Orwell-Updated", "george.new@test.com", 1903, "British");
        updatedAuthor.setId(1L);

        when(authorRepository.findById(1L)).thenReturn(Optional.of(author1));
        when(authorRepository.save(any(Author.class))).thenReturn(updatedAuthor);

        Author result = authorService.updateAuthor(1L, updateDetails);

        assertThat(result.getLastName()).isEqualTo("Orwell-Updated");
        assertThat(result.getEmail()).isEqualTo("george.new@test.com");
        verify(authorRepository).findById(1L);
        verify(authorRepository).save(any(Author.class));
    }

    @Test
    void updateAuthor_WhenAuthorNotFound_ShouldThrowException() {
        Author updateDetails = new Author("Ghost", "Author", "ghost@test.com", 1990, "Unknown");

        when(authorRepository.findById(99L)).thenReturn(Optional.empty());

        assertThatThrownBy(() -> authorService.updateAuthor(99L, updateDetails))
                .isInstanceOf(RuntimeException.class)
                .hasMessageContaining("Author not found with id: 99");

        verify(authorRepository).findById(99L);
        verify(authorRepository, never()).save(any());
    }

    @Test
    void getAuthorById_WhenExists_ShouldReturnAuthor() {
        when(authorRepository.findById(1L)).thenReturn(Optional.of(author1));

        Optional<Author> result = authorService.getAuthorById(1L);

        assertThat(result).isPresent();
        assertThat(result.get().getFirstName()).isEqualTo("George");
    }

    @Test
    void getAuthorById_WhenNotExists_ShouldReturnEmpty() {
        when(authorRepository.findById(99L)).thenReturn(Optional.empty());

        Optional<Author> result = authorService.getAuthorById(99L);

        assertThat(result).isEmpty();
    }

    @Test
    void deleteAuthor_ShouldCallRepositoryDeleteById() {
        doNothing().when(authorRepository).deleteById(1L);

        authorService.deleteAuthor(1L);

        verify(authorRepository, times(1)).deleteById(1L);
    }

    @Test
    void findByNationality_ShouldReturnMatchingAuthors() {
        when(authorRepository.findByNationality("British")).thenReturn(Arrays.asList(author1, author2));

        List<Author> result = authorService.findByNationality("British");

        assertThat(result).hasSize(2);
        verify(authorRepository).findByNationality("British");
    }

    @Test
    void findByEmail_WhenExists_ShouldReturnAuthor() {
        when(authorRepository.findByEmail("george.orwell@test.com")).thenReturn(Optional.of(author1));

        Optional<Author> result = authorService.findByEmail("george.orwell@test.com");

        assertThat(result).isPresent();
        assertThat(result.get().getFirstName()).isEqualTo("George");
    }
}
