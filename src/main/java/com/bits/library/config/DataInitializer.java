package com.bits.library.config;

import com.bits.library.entity.Author;
import com.bits.library.entity.Book;
import com.bits.library.repository.AuthorRepository;
import com.bits.library.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements CommandLineRunner {

    private final AuthorRepository authorRepository;
    private final BookRepository bookRepository;

    @Autowired
    public DataInitializer(AuthorRepository authorRepository, BookRepository bookRepository) {
        this.authorRepository = authorRepository;
        this.bookRepository = bookRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        Author author1 = authorRepository.save(new Author("George", "Orwell", "george.orwell@books.com", 1903, "British"));
        Author author2 = authorRepository.save(new Author("J.K.", "Rowling", "jk.rowling@books.com", 1965, "British"));
        Author author3 = authorRepository.save(new Author("Ernest", "Hemingway", "ernest.hemingway@books.com", 1899, "American"));
        Author author4 = authorRepository.save(new Author("Mark", "Twain", "mark.twain@books.com", 1835, "American"));
        Author author5 = authorRepository.save(new Author("Leo", "Tolstoy", "leo.tolstoy@books.com", 1828, "Russian"));
        Author author6 = authorRepository.save(new Author("Fyodor", "Dostoevsky", "fyodor.dostoevsky@books.com", 1821, "Russian"));
        Author author7 = authorRepository.save(new Author("Gabriel", "Garcia Marquez", "gabriel.marquez@books.com", 1927, "Colombian"));
        Author author8 = authorRepository.save(new Author("Haruki", "Murakami", "haruki.murakami@books.com", 1949, "Japanese"));
        Author author9 = authorRepository.save(new Author("Agatha", "Christie", "agatha.christie@books.com", 1890, "British"));
        Author author10 = authorRepository.save(new Author("Franz", "Kafka", "franz.kafka@books.com", 1883, "Czech"));

        bookRepository.save(new Book("1984", "978-0-452-28423-4", "Dystopian Fiction", 1949, 12.99, author1));
        bookRepository.save(new Book("Animal Farm", "978-0-452-28424-1", "Political Satire", 1945, 9.99, author1));
        bookRepository.save(new Book("Harry Potter and the Philosopher's Stone", "978-0-7475-3269-9", "Fantasy", 1997, 14.99, author2));
        bookRepository.save(new Book("Harry Potter and the Chamber of Secrets", "978-0-7475-3849-3", "Fantasy", 1998, 14.99, author2));
        bookRepository.save(new Book("The Old Man and the Sea", "978-0-684-80122-3", "Literary Fiction", 1952, 11.99, author3));
        bookRepository.save(new Book("Adventures of Huckleberry Finn", "978-0-486-28061-5", "Adventure", 1884, 8.99, author4));
        bookRepository.save(new Book("War and Peace", "978-0-14-303943-3", "Historical Fiction", 1869, 19.99, author5));
        bookRepository.save(new Book("Crime and Punishment", "978-0-14-305814-4", "Psychological Fiction", 1866, 13.99, author6));
        bookRepository.save(new Book("One Hundred Years of Solitude", "978-0-06-088328-7", "Magical Realism", 1967, 15.99, author7));
        bookRepository.save(new Book("Norwegian Wood", "978-0-375-70402-7", "Literary Fiction", 1987, 13.99, author8));

        System.out.println("=== Data Initialization Complete ===");
        System.out.println("Inserted 10 Authors and 10 Books into the database.");
    }
}
