import { useState } from 'react'
import './App.css'

export default function App() {
  const [plans, setPlans] = useState([])
  const [item, setItem] = useState('')

  function addPlan(event) {
    event.preventDefault()
    const trimmedItem = item.trim()
    if (!trimmedItem) return

    setPlans((currentPlans) => [
      ...currentPlans,
      { id: crypto.randomUUID(), item: trimmedItem },
    ])
    setItem('')
  }

  function removePlan(id) {
    setPlans((currentPlans) => currentPlans.filter((plan) => plan.id !== id))
  }

  return (
    <main className="app-shell">
      <section className="plan-card" aria-labelledby="page-title">
        <h1 id="page-title">Today&apos;s Plan</h1>
        <form className="plan-form" onSubmit={addPlan}>
          <label htmlFor="plan-item">Add a task</label>
          <div className="input-row">
            <input
              id="plan-item"
              value={item}
              onChange={(event) => setItem(event.target.value)}
              placeholder="e.g. Finish project work"
              maxLength="200"
            />
            <button type="submit" disabled={!item.trim()}>Add plan</button>
          </div>
        </form>

        <h2>Your plans</h2>
        {plans.length === 0 ? (
          <p className="message">No plans yet. Add your first one above.</p>
        ) : (
          <ul className="plan-list">
            {plans.map((plan) => (
              <li key={plan.id}>
                <span>{plan.item}</span>
                <button
                  className="remove-button"
                  type="button"
                  onClick={() => removePlan(plan.id)}
                >
                  Remove
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  )
}
