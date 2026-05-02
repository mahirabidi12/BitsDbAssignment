package com.bits.library.repository;

import com.bits.library.entity.Author;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface AuthorRepository extends JpaRepository<Author, Long> {

    List<Author> findByNationality(String nationality);

    Optional<Author> findByEmail(String email);
}
