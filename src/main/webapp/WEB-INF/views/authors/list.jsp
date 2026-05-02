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
        <h1>Authors</h1>
        <a href="/authors/new" class="btn btn-gold">
            &#43; Add New Author
        </a>
    </div>

    <div class="card">
        <div class="card-header">
            All Authors
            <span style="float:right; background: rgba(240,192,64,0.25); color: #f0c040; border-radius: 20px; padding: 0.1rem 0.75rem; font-size: 0.85rem;">
                <c:out value="${authors.size()}"/> total
            </span>
        </div>
        <div class="card-body" style="padding: 0;">
            <c:choose>
                <c:when test="${empty authors}">
                    <div class="empty-state">
                        <div class="empty-state-icon">&#128100;</div>
                        <h3>No Authors Found</h3>
                        <p>Start by adding your first author.</p>
                        <a href="/authors/new" class="btn btn-gold" style="margin-top:1rem;">Add First Author</a>
                    </div>
                </c:when>
                <c:otherwise>
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Birth Year</th>
                                    <th>Nationality</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <c:forEach var="author" items="${authors}" varStatus="status">
                                    <tr>
                                        <td style="color: #999; font-size: 0.85rem;">${status.count}</td>
                                        <td>
                                            <strong style="color: #1a2b4a;">${author.firstName} ${author.lastName}</strong>
                                        </td>
                                        <td style="color: #555;">
                                            <a href="mailto:${author.email}" style="color: #1a2b4a; text-decoration: none;">
                                                ${author.email}
                                            </a>
                                        </td>
                                        <td>${author.birthYear}</td>
                                        <td>
                                            <span class="badge badge-nationality">${author.nationality}</span>
                                        </td>
                                        <td>
                                            <div class="btn-actions">
                                                <a href="/authors/edit/${author.id}" class="btn btn-warning btn-sm">
                                                    &#9998; Edit
                                                </a>
                                                <a href="/authors/delete/${author.id}"
                                                   class="btn btn-danger btn-sm"
                                                   onclick="return confirm('Delete author \'${author.firstName} ${author.lastName}\'? This will also delete all their books.');">
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
