<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ include file="../layout/header.jsp" %>

<div class="container">

    <c:if test="${not empty errorMessage}">
        <div class="alert alert-danger">&#9888; ${errorMessage}</div>
    </c:if>

    <div class="page-header">
        <h1>${isEdit ? 'Edit Book' : 'Add New Book'}</h1>
        <a href="/books" class="btn btn-secondary">&#8592; Back to Books</a>
    </div>

    <div class="card" style="max-width: 750px;">
        <div class="card-header">
            ${isEdit ? 'Update Book Details' : 'New Book Information'}
        </div>
        <div class="card-body">
            <form action="${formAction}" method="post">

                <div class="form-group">
                    <label class="form-label" for="title">Title <span style="color:#dc3545;">*</span></label>
                    <input type="text"
                           id="title"
                           name="title"
                           class="form-control"
                           placeholder="Enter book title"
                           value="${isEdit ? book.title : ''}"
                           required />
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label" for="isbn">ISBN <span style="color:#dc3545;">*</span></label>
                        <input type="text"
                               id="isbn"
                               name="isbn"
                               class="form-control"
                               placeholder="e.g. 978-0-000-00000-0"
                               value="${isEdit ? book.isbn : ''}"
                               required />
                        <small style="color: #6b7a8d; font-size: 0.82rem; margin-top: 0.3rem; display: block;">
                            Must be unique across all books.
                        </small>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="genre">Genre <span style="color:#dc3545;">*</span></label>
                        <input type="text"
                               id="genre"
                               name="genre"
                               class="form-control"
                               placeholder="e.g. Fiction, Mystery, Fantasy"
                               value="${isEdit ? book.genre : ''}"
                               required />
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label" for="publishedYear">Published Year <span style="color:#dc3545;">*</span></label>
                        <input type="number"
                               id="publishedYear"
                               name="publishedYear"
                               class="form-control"
                               placeholder="e.g. 2020"
                               min="1000"
                               max="2100"
                               value="${isEdit ? book.publishedYear : ''}"
                               required />
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="price">Price (USD) <span style="color:#dc3545;">*</span></label>
                        <input type="number"
                               id="price"
                               name="price"
                               class="form-control"
                               placeholder="e.g. 14.99"
                               step="0.01"
                               min="0"
                               value="${isEdit ? book.price : ''}"
                               required />
                    </div>
                </div>

                <div class="form-group">
                    <label class="form-label" for="authorId">Author <span style="color:#dc3545;">*</span></label>
                    <select id="authorId" name="authorId" class="form-control" required>
                        <option value="">-- Select an Author --</option>
                        <c:forEach var="author" items="${authors}">
                            <option value="${author.id}"
                                ${isEdit && book.author.id == author.id ? 'selected' : ''}>
                                ${author.firstName} ${author.lastName} (${author.nationality})
                            </option>
                        </c:forEach>
                    </select>
                    <small style="color: #6b7a8d; font-size: 0.82rem; margin-top: 0.3rem; display: block;">
                        <a href="/authors/new" target="_blank" style="color: #1a2b4a;">Add a new author</a> if not listed.
                    </small>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn btn-gold">
                        ${isEdit ? '&#10003; Update Book' : '&#43; Save Book'}
                    </button>
                    <a href="/books" class="btn btn-secondary">Cancel</a>
                </div>

            </form>
        </div>
    </div>
</div>

<div class="footer">
    &copy; 2024 Library Management System &mdash; Built with Spring Boot, JPA &amp; JSP
</div>
</body>
</html>
