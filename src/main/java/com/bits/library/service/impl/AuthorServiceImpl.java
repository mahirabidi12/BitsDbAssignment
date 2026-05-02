package com.bits.library.service.impl;

import com.bits.library.entity.Author;
import com.bits.library.repository.AuthorRepository;
import com.bits.library.service.AuthorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class AuthorServiceImpl implements AuthorService {

    private final AuthorRepository authorRepository;

    @Autowired
    public AuthorServiceImpl(AuthorRepository authorRepository) {
        this.authorRepository = authorRepository;
    }

    @Override
    @Transactional(readOnly = true)
    public List<Author> getAllAuthors() {
        return authorRepository.findAll();
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Author> getAuthorById(Long id) {
        return authorRepository.findById(id);
    }

    @Override
    public Author saveAuthor(Author author) {
        return authorRepository.save(author);
    }

    @Override
    public Author updateAuthor(Long id, Author authorDetails) {
        Author existingAuthor = authorRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Author not found with id: " + id));

        existingAuthor.setFirstName(authorDetails.getFirstName());
        existingAuthor.setLastName(authorDetails.getLastName());
        existingAuthor.setEmail(authorDetails.getEmail());
        existingAuthor.setBirthYear(authorDetails.getBirthYear());
        existingAuthor.setNationality(authorDetails.getNationality());

        return authorRepository.save(existingAuthor);
    }

    @Override
    public void deleteAuthor(Long id) {
        authorRepository.deleteById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Author> findByNationality(String nationality) {
        return authorRepository.findByNationality(nationality);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Author> findByEmail(String email) {
        return authorRepository.findByEmail(email);
    }
}
