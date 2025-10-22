"use client";

export default function PlannerPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-4xl font-bold text-[var(--uq-purple)]">My Planner</h1>
      <p className="text-gray-600">Drag courses into terms (placeholder for now).</p>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {["Y1 • Sem 1","Y1 • Sem 2","Y2 • Sem 1","Y2 • Sem 2","Y3 • Sem 1","Y3 • Sem 2"].map(t => (
          <section key={t} className="card">
            <h2 className="text-lg font-semibold mb-3">{t}</h2>
            <div className="grid grid-cols-2 gap-3">
              {Array.from({ length: 4 }).map((_, i) => (
                <div key={i} className="rounded-lg border border-dashed p-4 text-sm text-gray-500 bg-[var(--uq-light)]/50">
                  Empty
                </div>
              ))}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
}
