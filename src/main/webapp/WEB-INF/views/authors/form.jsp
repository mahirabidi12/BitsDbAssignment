<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ include file="../layout/header.jsp" %>

<div class="container">

    <c:if test="${not empty errorMessage}">
        <div class="alert alert-danger">&#9888; ${errorMessage}</div>
    </c:if>

    <div class="page-header">
        <h1>${isEdit ? 'Edit Author' : 'Add New Author'}</h1>
        <a href="/authors" class="btn btn-secondary">&#8592; Back to Authors</a>
    </div>

    <div class="card" style="max-width: 700px;">
        <div class="card-header">
            ${isEdit ? 'Update Author Details' : 'New Author Information'}
        </div>
        <div class="card-body">
            <form action="${formAction}" method="post">

                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label" for="firstName">First Name <span style="color:#dc3545;">*</span></label>
                        <input type="text"
                               id="firstName"
                               name="firstName"
                               class="form-control"
                               placeholder="Enter first name"
                               value="${isEdit ? author.firstName : ''}"
                               required />
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="lastName">Last Name <span style="color:#dc3545;">*</span></label>
                        <input type="text"
                               id="lastName"
                               name="lastName"
                               class="form-control"
                               placeholder="Enter last name"
                               value="${isEdit ? author.lastName : ''}"
                               required />
                    </div>
                </div>

                <div class="form-group">
                    <label class="form-label" for="email">Email Address <span style="color:#dc3545;">*</span></label>
                    <input type="email"
                           id="email"
                           name="email"
                           class="form-control"
                           placeholder="author@example.com"
                           value="${isEdit ? author.email : ''}"
                           required />
                    <small style="color: #6b7a8d; font-size: 0.82rem; margin-top: 0.3rem; display: block;">
                        Must be unique across all authors.
                    </small>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label" for="birthYear">Birth Year <span style="color:#dc3545;">*</span></label>
                        <input type="number"
                               id="birthYear"
                               name="birthYear"
                               class="form-control"
                               placeholder="e.g. 1975"
                               min="1000"
                               max="2010"
                               value="${isEdit ? author.birthYear : ''}"
                               required />
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="nationality">Nationality <span style="color:#dc3545;">*</span></label>
                        <input type="text"
                               id="nationality"
                               name="nationality"
                               class="form-control"
                               placeholder="e.g. British, American, Russian"
                               value="${isEdit ? author.nationality : ''}"
                               required />
                    </div>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn btn-gold">
                        ${isEdit ? '&#10003; Update Author' : '&#43; Save Author'}
                    </button>
                    <a href="/authors" class="btn btn-secondary">Cancel</a>
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
