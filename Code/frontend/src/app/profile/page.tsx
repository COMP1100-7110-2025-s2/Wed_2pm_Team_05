"use client";

export default function ProfilePage() {
  return (
    <div className="space-y-8">
      <h1 className="text-4xl font-bold text-[var(--uq-purple)]">Profile</h1>
      <div className="grid gap-4 max-w-xl">
        <button className="btn btn-outline">Change Password</button>
        <button className="btn btn-outline">Change Email</button>
        <a href="/" className="btn btn-secondary text-center">Sign Out</a>
      </div>
    </div>
  );
}
