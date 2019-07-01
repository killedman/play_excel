#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def main():
    databse = 'wacai.db'
    sql_create_table = "table.sql"
    sql_create_borrowing_and_lending_table = """CREATE TABLE "borrowing_and_lending" (
                                              "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                              "borrowing_type" TEXT NOT NULL,
                                              "borrowing_date" DATETIME NOT NULL,
                                              "borrowing_account" TEXT NOT NULL,
                                              "account" TEXT NOT NULL,
                                              "amount_of_money" REAL NOT NULL,
                                              "remark" TEXT NOT NULL,
                                              "book" TEXT NOT NULL DEFAULT "日常账本"
                                            );"""
    sql_create_expenses_table = """CREATE TABLE "expenses" (
                                  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                  "main_category" TEXT NOT NULL,
                                  "small_category" TEXT NOT NULL,
                                  "account" TEXT NOT NULL,
                                  "currency" TEXT NOT NULL DEFAULT "人民币",
                                  "project" TEXT NOT NULL DEFAULT "日常",
                                  "merchant" TEXT NOT NULL,
                                  "reimburse" TEXT NOT NULL DEFAULT "非报销",
                                  "date" DATETIME NOT NULL,
                                  "amount" REAL NOT NULL,
                                  "member_money" TEXT NOT NULL,
                                  "remark" TEXT NOT NULL,
                                  "book" TEXT NOT NULL DEFAULT "日常账本"
                                );"""
    sql_create_income_table = """CREATE TABLE "income" (
                                  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                  "major_income_category" TEXT NOT NULL,
                                  "account" TEXT NOT NULL,
                                  "currency" TEXT NOT NULL DEFAULT "人民币",
                                  "project" TEXT NOT NULL DEFAULT "日常",
                                  "payer" TEXT NOT NULL,
                                  "income_date" DATETIME NOT NULL,
                                  "amount_of_income" REAL NOT NULL,
                                  "amount_of_member" REAL NOT NULL,
                                  "remark" TEXT NOT NULL,
                                  "book" TEXT NOT NULL DEFAULT "日常账本"
                                );"""
    sql_create_payment_repayment_table = """CREATE TABLE "payment_repayment" (
                                          "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                          "borrowing_type" TEXT NOT NULL,
                                          "borrowing_date" DATETIME NOT NULL,
                                          "borrowing_account" TEXT NOT NULL,
                                          "account" TEXT NOT NULL,
                                          "amount_of_money" REAL NOT NULL,
                                          "interest" REAL,
                                          "remark" TEXT NOT NULL,
                                          "book" TEXT NOT NULL DEFAULT "日常账本"
                                        );"""
    sql_create_transfer_table = """CREATE TABLE "transfer" (
                                  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                  "transfer_account" TEXT NOT NULL,
                                  "transfer_currency" TEXT NOT NULL DEFAULT "人民币",
                                  "transfer_amount" REAL NOT NULL,
                                  "transfer_to_account" REAL NOT NULL,
                                  "transfer_to_currency" TEXT NOT NULL,
                                  "transfer_to_amount" REAL NOT NULL,
                                  "transfer_date" DATETIME NOT NULL,
                                  "remark" TEXT NOT NULL,
                                  "book" TEXT NOT NULL DEFAULT "日常账本"
                                )"""
    conn = create_connection(databse)
    if conn is not None:
        create_table(conn, sql_create_borrowing_and_lending_table)
        create_table(conn, sql_create_expenses_table)
        create_table(conn, sql_create_income_table)
        create_table(conn, sql_create_payment_repayment_table)
        create_table(conn, sql_create_transfer_table)
    else:
        print("Error! connot crate the database connection")

if __name__ == "__main__":
    main()