<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${pageTitle} - Library Management System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f4f8;
            color: #333;
            min-height: 100vh;
        }

        /* ===== NAVBAR ===== */
        .navbar {
            background: linear-gradient(135deg, #1a2b4a 0%, #0d1b2e 100%);
            padding: 0 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .navbar-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 1200px;
            margin: 0 auto;
            height: 64px;
        }

        .navbar-brand {
            display: flex;
            align-items: center;
            text-decoration: none;
            gap: 10px;
        }

        .navbar-brand-icon {
            font-size: 1.6rem;
        }

        .navbar-brand-text {
            color: #f0c040;
            font-size: 1.3rem;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        .navbar-nav {
            display: flex;
            list-style: none;
            gap: 0.5rem;
            align-items: center;
        }

        .navbar-nav a {
            color: #cdd9ea;
            text-decoration: none;
            padding: 0.5rem 1.1rem;
            border-radius: 6px;
            font-size: 0.95rem;
            font-weight: 500;
            transition: background 0.2s, color 0.2s;
        }

        .navbar-nav a:hover,
        .navbar-nav a.active {
            background: rgba(240, 192, 64, 0.15);
            color: #f0c040;
        }

        /* ===== CONTAINER ===== */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1.5rem;
        }

        /* ===== PAGE HEADER ===== */
        .page-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
        }

        .page-header h1 {
            font-size: 1.8rem;
            font-weight: 700;
            color: #1a2b4a;
            position: relative;
            padding-bottom: 0.4rem;
        }

        .page-header h1::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 48px;
            height: 3px;
            background: #f0c040;
            border-radius: 2px;
        }

        /* ===== ALERTS ===== */
        .alert {
            padding: 0.85rem 1.2rem;
            border-radius: 8px;
            margin-bottom: 1.2rem;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .alert-success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .alert-danger {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        .alert-info {
            background-color: #d1ecf1;
            color: #0c5460;
            border: 1px solid #bee5eb;
        }

        /* ===== CARD ===== */
        .card {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 2px 16px rgba(26,43,74,0.08);
            overflow: hidden;
        }

        .card-header {
            background: linear-gradient(135deg, #1a2b4a 0%, #233a5e 100%);
            color: #fff;
            padding: 1rem 1.5rem;
            font-size: 1rem;
            font-weight: 600;
            letter-spacing: 0.3px;
        }

        .card-body {
            padding: 1.5rem;
        }

        /* ===== TABLE ===== */
        .table-responsive {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.93rem;
        }

        thead {
            background: #1a2b4a;
            color: #fff;
        }

        thead th {
            padding: 0.85rem 1rem;
            text-align: left;
            font-weight: 600;
            font-size: 0.88rem;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            white-space: nowrap;
        }

        tbody tr {
            border-bottom: 1px solid #e8edf4;
            transition: background 0.15s;
        }

        tbody tr:hover {
            background-color: #f5f8ff;
        }

        tbody td {
            padding: 0.85rem 1rem;
            color: #444;
            vertical-align: middle;
        }

        .badge {
            display: inline-block;
            padding: 0.25rem 0.65rem;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
            background: #e8edf4;
            color: #1a2b4a;
        }

        .badge-genre {
            background: #eef2ff;
            color: #3b4fc4;
        }

        .badge-nationality {
            background: #fef3c7;
            color: #92400e;
        }

        /* ===== BUTTONS ===== */
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.5rem 1.1rem;
            border: none;
            border-radius: 7px;
            font-size: 0.88rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.2s;
            white-space: nowrap;
        }

        .btn-primary {
            background: #1a2b4a;
            color: #fff;
        }

        .btn-primary:hover {
            background: #233a5e;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(26,43,74,0.2);
        }

        .btn-gold {
            background: #f0c040;
            color: #1a2b4a;
        }

        .btn-gold:hover {
            background: #e8b530;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(240,192,64,0.3);
        }

        .btn-success {
            background: #28a745;
            color: #fff;
        }

        .btn-success:hover {
            background: #218838;
            transform: translateY(-1px);
        }

        .btn-warning {
            background: #f0c040;
            color: #1a2b4a;
            font-size: 0.82rem;
            padding: 0.38rem 0.85rem;
        }

        .btn-warning:hover {
            background: #e8b530;
        }

        .btn-danger {
            background: #dc3545;
            color: #fff;
            font-size: 0.82rem;
            padding: 0.38rem 0.85rem;
        }

        .btn-danger:hover {
            background: #c82333;
        }

        .btn-secondary {
            background: #6c757d;
            color: #fff;
        }

        .btn-secondary:hover {
            background: #5a6268;
        }

        .btn-outline {
            background: transparent;
            border: 2px solid #1a2b4a;
            color: #1a2b4a;
        }

        .btn-outline:hover {
            background: #1a2b4a;
            color: #fff;
        }

        .btn-sm {
            padding: 0.32rem 0.75rem;
            font-size: 0.8rem;
        }

        .btn-actions {
            display: flex;
            gap: 0.4rem;
        }

        /* ===== FORMS ===== */
        .form-group {
            margin-bottom: 1.2rem;
        }

        .form-label {
            display: block;
            margin-bottom: 0.4rem;
            font-weight: 600;
            font-size: 0.9rem;
            color: #1a2b4a;
        }

        .form-control {
            width: 100%;
            padding: 0.65rem 0.9rem;
            border: 1.5px solid #d0d9e8;
            border-radius: 7px;
            font-size: 0.93rem;
            color: #333;
            background: #fff;
            transition: border-color 0.2s, box-shadow 0.2s;
            outline: none;
        }

        .form-control:focus {
            border-color: #1a2b4a;
            box-shadow: 0 0 0 3px rgba(26,43,74,0.1);
        }

        select.form-control {
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%231a2b4a' d='M1 1l5 5 5-5'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 12px center;
            padding-right: 2.5rem;
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }

        .form-actions {
            display: flex;
            gap: 0.75rem;
            margin-top: 1.5rem;
            padding-top: 1.2rem;
            border-top: 1px solid #e8edf4;
        }

        /* ===== SEARCH FORM ===== */
        .search-form {
            display: flex;
            gap: 0.75rem;
            align-items: flex-end;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }

        .search-form .form-group {
            margin-bottom: 0;
            flex: 1;
            min-width: 200px;
        }

        /* ===== STATS ===== */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .stat-card {
            background: #fff;
            border-radius: 10px;
            padding: 1.2rem 1.5rem;
            box-shadow: 0 2px 8px rgba(26,43,74,0.07);
            border-left: 4px solid #f0c040;
        }

        .stat-card .stat-value {
            font-size: 2rem;
            font-weight: 700;
            color: #1a2b4a;
            line-height: 1;
        }

        .stat-card .stat-label {
            font-size: 0.85rem;
            color: #6b7a8d;
            margin-top: 0.3rem;
        }

        /* ===== EMPTY STATE ===== */
        .empty-state {
            text-align: center;
            padding: 3rem;
            color: #6b7a8d;
        }

        .empty-state-icon {
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }

        .empty-state h3 {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
            color: #444;
        }

        /* ===== FOOTER ===== */
        .footer {
            text-align: center;
            padding: 1.5rem;
            color: #6b7a8d;
            font-size: 0.85rem;
            margin-top: 3rem;
            border-top: 1px solid #e0e7ef;
        }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .form-row {
                grid-template-columns: 1fr;
            }
            .page-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 1rem;
            }
            .navbar-inner {
                flex-wrap: wrap;
                height: auto;
                padding: 0.75rem 0;
            }
        }
    </style>
</head>
<body>
<nav class="navbar">
    <div class="navbar-inner">
        <a href="/index" class="navbar-brand">
            <span class="navbar-brand-icon">&#128218;</span>
            <span class="navbar-brand-text">Library Management System</span>
        </a>
        <ul class="navbar-nav">
            <li><a href="/books">Books</a></li>
            <li><a href="/authors">Authors</a></li>
            <li><a href="/books/byNationality">By Nationality</a></li>
            <li><a href="/h2-console" target="_blank">H2 Console</a></li>
        </ul>
    </div>
</nav>
