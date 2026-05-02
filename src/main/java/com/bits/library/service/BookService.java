package com.bits.library.service;

import com.bits.library.entity.Book;

import java.util.List;
import java.util.Optional;

public interface BookService {

    List<Book> getAllBooks();

    Optional<Book> getBookById(Long id);

    Book saveBook(Book book);

    Book updateBook(Long id, Book book);

    void deleteBook(Long id);

    List<Book> findByGenre(String genre);

    List<Book> findByAuthorId(Long authorId);

    List<Book> findByAuthorNationality(String nationality);
}
