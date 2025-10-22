"use client";

export default function LoginPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] gap-6">
      <h1 className="text-4xl font-bold text-[var(--uq-purple)]">Login</h1>
      <form className="bg-white p-8 rounded-2xl shadow w-full max-w-md space-y-4">
        <input placeholder="Username" className="w-full border px-4 py-3 rounded-lg" />
        <input type="password" placeholder="Password" className="w-full border px-4 py-3 rounded-lg" />
        <button className="btn btn-primary w-full py-3 rounded-lg">Login</button>
      </form>
    </div>
  );
}
