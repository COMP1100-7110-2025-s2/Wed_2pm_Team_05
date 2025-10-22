"use client";

import Link from "next/link";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-[var(--uq-light)] to-white text-center space-y-10">
      <div>
        <h1 className="text-6xl font-extrabold text-[var(--uq-purple)] drop-shadow-sm">
          UQ
        </h1>
        <p className="text-2xl text-gray-700 font-medium">Courses</p>
        <p className="mt-4 text-gray-600 max-w-md">
          Login with your UQ Courses account, create an account, or continue as a
          guest.
        </p>
      </div>

      <div className="flex flex-wrap justify-center gap-6 mt-6">
        <Link
          href="/login"
          className="btn btn-primary px-8 py-3 text-lg rounded-xl shadow-md"
        >
          Login
        </Link>
        <Link
          href="/signup"
          className="btn btn-secondary px-8 py-3 text-lg rounded-xl shadow-md"
        >
          Sign Up
        </Link>
        <Link
          href="/guest"
          className="btn btn-outline px-8 py-3 text-lg rounded-xl shadow-md"
        >
          Continue as Guest
        </Link>
      </div>

      <footer className="text-sm text-gray-500 absolute bottom-10">
        © 2025 UQ Courses — Design inspired by your prototype 🌈
      </footer>
    </main>
  );
}
