"use client";

export default function SignUpPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] gap-6">
      <h1 className="text-4xl font-bold text-[var(--uq-purple)]">Create account</h1>
      <form className="bg-white p-8 rounded-2xl shadow w-full max-w-md space-y-4">
        <input placeholder="Username" className="w-full border px-4 py-3 rounded-lg" />
        <input type="email" placeholder="Email" className="w-full border px-4 py-3 rounded-lg" />
        <input type="password" placeholder="Password (min 8 chars)" className="w-full border px-4 py-3 rounded-lg" />
        <button className="btn btn-secondary w-full py-3 rounded-lg">Sign Up</button>
      </form>
    </div>
  );
}
