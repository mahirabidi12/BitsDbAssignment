<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ include file="../layout/header.jsp" %>

<div class="container">

    <div class="page-header">
        <h1>Books by Author Nationality</h1>
        <a href="/books" class="btn btn-secondary">&#8592; Back to Books</a>
    </div>

    <div class="alert alert-info">
        &#128221; This page demonstrates an <strong>INNER JOIN</strong> query:
        <code style="background: rgba(0,0,0,0.08); padding: 0.1rem 0.4rem; border-radius: 4px; font-size: 0.88rem;">
            SELECT b FROM Book b INNER JOIN b.author a WHERE a.nationality = :nationality
        </code>
    </div>

    <!-- Search Form -->
    <div class="card" style="margin-bottom: 1.5rem;">
        <div class="card-header">Search Books by Author Nationality</div>
        <div class="card-body">
            <form action="/books/byNationality" method="get" class="search-form">
                <div class="form-group">
                    <label class="form-label" for="nationality">Nationality</label>
                    <input type="text"
                           id="nationality"
                           name="nationality"
                           class="form-control"
                           placeholder="e.g. British, American, Russian, Japanese..."
                           value="${nationality != null ? nationality : ''}" />
                </div>
                <div style="display: flex; gap: 0.5rem; align-items: flex-end;">
                    <button type="submit" class="btn btn-primary">&#128269; Search</button>
                    <a href="/books/byNationality" class="btn btn-secondary">Clear</a>
                </div>
            </form>

            <!-- Quick filter buttons -->
            <div style="margin-top: 0.75rem;">
                <span style="font-size: 0.85rem; color: #6b7a8d; margin-right: 0.5rem;">Quick filters:</span>
                <a href="/books/byNationality?nationality=British" class="btn btn-sm btn-outline" style="margin: 0.2rem;">British</a>
                <a href="/books/byNationality?nationality=American" class="btn btn-sm btn-outline" style="margin: 0.2rem;">American</a>
                <a href="/books/byNationality?nationality=Russian" class="btn btn-sm btn-outline" style="margin: 0.2rem;">Russian</a>
                <a href="/books/byNationality?nationality=Japanese" class="btn btn-sm btn-outline" style="margin: 0.2rem;">Japanese</a>
                <a href="/books/byNationality?nationality=Colombian" class="btn btn-sm btn-outline" style="margin: 0.2rem;">Colombian</a>
                <a href="/books/byNationality?nationality=Czech" class="btn btn-sm btn-outline" style="margin: 0.2rem;">Czech</a>
            </div>
        </div>
    </div>

    <!-- Results -->
    <c:choose>
        <c:when test="${nationality == null || nationality == ''}">
            <div class="card">
                <div class="card-body">
                    <div class="empty-state">
                        <div class="empty-state-icon">&#127760;</div>
                        <h3>Enter a Nationality to Search</h3>
                        <p>Use the search form above or click a quick filter to find books by author nationality.</p>
                    </div>
                </div>
            </div>
        </c:when>
        <c:otherwise>
            <div class="card">
                <div class="card-header">
                    Results for nationality: "<strong>${nationality}</strong>"
                    <c:if test="${not empty books}">
                        <span style="float:right; background: rgba(240,192,64,0.25); color: #f0c040; border-radius: 20px; padding: 0.1rem 0.75rem; font-size: 0.85rem;">
                            ${books.size()} book(s) found
                        </span>
                    </c:if>
                </div>
                <div class="card-body" style="padding: 0;">
                    <c:choose>
                        <c:when test="${empty books}">
                            <div class="empty-state">
                                <div class="empty-state-icon">&#128214;</div>
                                <h3>No Books Found</h3>
                                <p>No books were found for authors with nationality: <strong>${nationality}</strong></p>
                                <p style="margin-top: 0.5rem; font-size: 0.9rem; color: #6b7a8d;">
                                    Try: British, American, Russian, Japanese, Colombian, Czech
                                </p>
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
                                            <th>Nationality</th>
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
                                                <td style="color: #1a2b4a; font-weight: 500;">
                                                    ${book.author.firstName} ${book.author.lastName}
                                                </td>
                                                <td>
                                                    <span class="badge badge-nationality">${book.author.nationality}</span>
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
        </c:otherwise>
    </c:choose>

</div>

<div class="footer">
    &copy; 2024 Library Management System &mdash; Built with Spring Boot, JPA &amp; JSP
</div>
</body>
</html>
