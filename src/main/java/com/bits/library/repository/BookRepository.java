package com.bits.library.repository;

import com.bits.library.entity.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BookRepository extends JpaRepository<Book, Long> {

    List<Book> findByGenre(String genre);

    List<Book> findByAuthorId(Long authorId);

    @Query("SELECT b FROM Book b INNER JOIN b.author a WHERE a.nationality = :nationality")
    List<Book> findByAuthorNationality(@Param("nationality") String nationality);
}
