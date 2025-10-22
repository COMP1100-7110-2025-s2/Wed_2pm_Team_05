import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Link from "next/link";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "UQ Courses",
  description: "Find and plan your university courses easily.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} flex min-h-screen bg-[var(--uq-light)] text-gray-800`}
      >
        {/* Sidebar */}
        <aside className="hidden md:flex flex-col justify-between w-64 bg-[var(--uq-purple)] text-white py-10 px-6">
          <div>
            <h1 className="text-3xl font-extrabold text-center mb-10">
              UQ Courses
            </h1>

            <nav className="space-y-4">
              <Link href="/courses" className="block hover:text-[var(--uq-accent)] transition">
                📘 Courses
              </Link>
              <Link href="/planner" className="block hover:text-[var(--uq-accent)] transition">
                🗓 Planner
              </Link>
              <Link href="/profile" className="block hover:text-[var(--uq-accent)] transition">
                👤 Profile
              </Link>
            </nav>
          </div>

          <Link
            href="/"
            className="text-center text-sm hover:text-[var(--uq-accent)] transition"
          >
            ↩ Sign Out
          </Link>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-10 bg-white rounded-tl-3xl md:rounded-none shadow-inner">
          {children}
        </main>
      </body>
    </html>
  );
}
