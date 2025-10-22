export default function CoursesPage() {
    return (
      <div className="space-y-6">
        <h1 className="text-4xl font-bold text-[var(--uq-purple)]">Courses</h1>
        <p className="text-gray-600">Search results will appear here.</p>
  
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[1,2,3,4,5,6].map(i => (
            <div key={i} className="card">
              <h3 className="font-semibold">Software Innovation</h3>
              <p className="text-sm text-gray-600">COMP1100 • Level 1 • Semester 1</p>
              <button className="btn btn-primary mt-4">View</button>
            </div>
          ))}
        </div>
      </div>
    );
  }
  