"use client";
import { useState } from "react";

export default function GuestPage() {
  const [q, setQ] = useState("");

  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] gap-8 text-center">
      <div>
        <h1 className="text-4xl font-extrabold text-[var(--uq-purple)]">Find your course</h1>
        <p className="text-gray-600 mt-2">Search for your course or degree</p>
      </div>

      <input
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder="e.g., COMP1100, Software, AI…"
        className="w-96 max-w-full px-5 py-3 border-2 border-[var(--uq-purple)] rounded-xl focus:outline-none focus:ring-4 focus:ring-[var(--uq-light)]"
      />

      <div className="flex gap-3 flex-wrap justify-center">
        <button className="btn btn-primary">Level</button>
        <button className="btn btn-secondary">Semester</button>
        <button className="btn btn-outline">Area of Study</button>
      </div>
    </div>
  );
}
