<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ include file="layout/header.jsp" %>

<div class="container">
    <div style="text-align:center; padding: 3rem 1rem 2rem;">
        <div style="font-size: 5rem; margin-bottom: 1rem;">&#128218;</div>
        <h1 style="font-size: 2.5rem; font-weight: 800; color: #1a2b4a; margin-bottom: 0.75rem;">
            Library Management System
        </h1>
        <p style="font-size: 1.1rem; color: #6b7a8d; max-width: 520px; margin: 0 auto 2.5rem;">
            Manage your library's collection of books and authors with ease.
            Add, edit, and explore your entire catalogue.
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="/books" class="btn btn-primary" style="font-size: 1rem; padding: 0.75rem 2rem;">
                &#128214; Browse Books
            </a>
            <a href="/authors" class="btn btn-gold" style="font-size: 1rem; padding: 0.75rem 2rem;">
                &#128100; Browse Authors
            </a>
            <a href="/books/byNationality" class="btn btn-outline" style="font-size: 1rem; padding: 0.75rem 2rem;">
                &#127760; By Nationality
            </a>
        </div>
    </div>

    <div class="stats-grid" style="margin-top: 1rem;">
        <div class="stat-card">
            <div class="stat-value">&#128214;</div>
            <div class="stat-label" style="font-size: 1rem; font-weight: 600; color: #1a2b4a; margin-top: 0.5rem;">Books Collection</div>
            <div class="stat-label">Browse and manage all books</div>
        </div>
        <div class="stat-card" style="border-left-color: #1a2b4a;">
            <div class="stat-value">&#128100;</div>
            <div class="stat-label" style="font-size: 1rem; font-weight: 600; color: #1a2b4a; margin-top: 0.5rem;">Author Profiles</div>
            <div class="stat-label">Manage author information</div>
        </div>
        <div class="stat-card" style="border-left-color: #28a745;">
            <div class="stat-value">&#127760;</div>
            <div class="stat-label" style="font-size: 1rem; font-weight: 600; color: #1a2b4a; margin-top: 0.5rem;">Search by Nationality</div>
            <div class="stat-label">Inner join query on authors</div>
        </div>
        <div class="stat-card" style="border-left-color: #dc3545;">
            <div class="stat-value">&#128203;</div>
            <div class="stat-label" style="font-size: 1rem; font-weight: 600; color: #1a2b4a; margin-top: 0.5rem;">H2 Database</div>
            <div class="stat-label">In-memory data storage</div>
        </div>
    </div>

    <div style="margin-top: 2rem; display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
        <div class="card">
            <div class="card-header">Quick Actions - Books</div>
            <div class="card-body">
                <p style="margin-bottom: 1rem; color: #6b7a8d; font-size: 0.93rem;">
                    Manage the library's book catalogue including title, ISBN, genre, price, and author assignments.
                </p>
                <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                    <a href="/books" class="btn btn-primary btn-sm">View All Books</a>
                    <a href="/books/new" class="btn btn-gold btn-sm">Add New Book</a>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header">Quick Actions - Authors</div>
            <div class="card-body">
                <p style="margin-bottom: 1rem; color: #6b7a8d; font-size: 0.93rem;">
                    Manage author profiles with their personal details, nationality, birth year, and contact information.
                </p>
                <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
                    <a href="/authors" class="btn btn-primary btn-sm">View All Authors</a>
                    <a href="/authors/new" class="btn btn-gold btn-sm">Add New Author</a>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="footer">
    &copy; 2024 Library Management System &mdash; Built with Spring Boot, JPA &amp; JSP
</div>
</body>
</html>
