<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ include file="../layout/header.jsp" %>

<div class="container">

    <c:if test="${not empty successMessage}">
        <div class="alert alert-success">&#10003; ${successMessage}</div>
    </c:if>
    <c:if test="${not empty errorMessage}">
        <div class="alert alert-danger">&#9888; ${errorMessage}</div>
    </c:if>

    <div class="page-header">
        <h1>Books</h1>
        <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
            <a href="/books/byNationality" class="btn btn-outline">
                &#127760; Search by Nationality
            </a>
            <a href="/books/new" class="btn btn-gold">
                &#43; Add New Book
            </a>
        </div>
    </div>

    <div class="card">
        <div class="card-header">
            All Books
            <span style="float:right; background: rgba(240,192,64,0.25); color: #f0c040; border-radius: 20px; padding: 0.1rem 0.75rem; font-size: 0.85rem;">
                <c:out value="${books.size()}"/> total
            </span>
        </div>
        <div class="card-body" style="padding: 0;">
            <c:choose>
                <c:when test="${empty books}">
                    <div class="empty-state">
                        <div class="empty-state-icon">&#128214;</div>
                        <h3>No Books Found</h3>
                        <p>Start by adding your first book to the library.</p>
                        <a href="/books/new" class="btn btn-gold" style="margin-top:1rem;">Add First Book</a>
                    </div>
                </c:when>
                <c:otherwise>
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Title</th>
                                    <th>ISBN</th>
                                    <th>Genre</th>
                                    <th>Year</th>
                                    <th>Price</th>
                                    <th>Author</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <c:forEach var="book" items="${books}" varStatus="status">
                                    <tr>
                                        <td style="color: #999; font-size: 0.85rem;">${status.count}</td>
                                        <td>
                                            <strong style="color: #1a2b4a;">${book.title}</strong>
                                        </td>
                                        <td style="font-family: monospace; font-size: 0.82rem; color: #666;">
                                            ${book.isbn}
                                        </td>
                                        <td>
                                            <span class="badge badge-genre">${book.genre}</span>
                                        </td>
                                        <td>${book.publishedYear}</td>
                                        <td>
                                            <strong style="color: #28a745;">
                                                $<fmt:formatNumber value="${book.price}" pattern="#,##0.00"/>
                                            </strong>
                                        </td>
                                        <td>
                                            <span style="color: #1a2b4a; font-weight: 500;">
                                                ${book.author.firstName} ${book.author.lastName}
                                            </span>
                                            <br/>
                                            <span class="badge badge-nationality" style="font-size: 0.72rem;">
                                                ${book.author.nationality}
                                            </span>
                                        </td>
                                        <td>
                                            <div class="btn-actions">
                                                <a href="/books/edit/${book.id}" class="btn btn-warning btn-sm">
                                                    &#9998; Edit
                                                </a>
                                                <a href="/books/delete/${book.id}"
                                                   class="btn btn-danger btn-sm"
                                                   onclick="return confirm('Delete book \'${book.title}\'?');">
                                                    &#128465; Delete
                                                </a>
                                            </div>
                                        </td>
                                    </tr>
                                </c:forEach>
                            </tbody>
                        </table>
                    </div>
                </c:otherwise>
            </c:choose>
        </div>
    </div>
</div>

<div class="footer">
    &copy; 2024 Library Management System &mdash; Built with Spring Boot, JPA &amp; JSP
</div>
</body>
</html>
