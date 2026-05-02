package com.bits.library.service;

import com.bits.library.entity.Author;

import java.util.List;
import java.util.Optional;

public interface AuthorService {

    List<Author> getAllAuthors();

    Optional<Author> getAuthorById(Long id);

    Author saveAuthor(Author author);

    Author updateAuthor(Long id, Author author);

    void deleteAuthor(Long id);

    List<Author> findByNationality(String nationality);

    Optional<Author> findByEmail(String email);
}
