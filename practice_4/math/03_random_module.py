import json
import os
import random
import math
from datetime import datetime, timedelta

OUTPUT_DIR = "practice_4/json/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Seed for reproducibility in test/CI contexts — remove for true randomness
random.seed(42)

# --- Example 1: random.random() and random.uniform() for simulation JSON ---
raw_sim_config = '''
{
    "simulation": "MonteCarloRisk",
    "trials": 10,
    "asset": {
        "name": "PortfolioX",
        "initial_value": 100000,
        "annual_return_mu": 0.08,
        "annual_volatility_sigma": 0.18,
        "horizon_years": 5
    }
}
'''

try:
    sim_cfg = json.loads(raw_sim_config)
except json.JSONDecodeError as e:
    raise SystemExit(f"Sim config parse error at line {e.lineno}: {e.msg}")

asset  = sim_cfg["asset"]
trials = []

for i in range(sim_cfg["trials"]):
    value = asset["initial_value"]
    yearly = []
    for _ in range(asset["horizon_years"]):
        # Geometric Brownian Motion step: r ~ N(μ, σ) approximated via uniform
        # random.gauss(mu, sigma) gives normally-distributed annual return
        annual_r = random.gauss(asset["annual_return_mu"], asset["annual_volatility_sigma"])
        value = round(value * (1 + annual_r), 2)
        yearly.append(value)
    trials.append({
        "trial_id":    i + 1,
        "final_value": value,
        "trajectory":  yearly,
        # flag drawdown scenarios
        "is_loss":     value < asset["initial_value"]
    })

final_values  = [t["final_value"] for t in trials]
loss_count    = sum(1 for t in trials if t["is_loss"])
print(f"Simulation: {sim_cfg['simulation']}")
print(f"  Trials   : {sim_cfg['trials']}")
print(f"  Best     : ${max(final_values):>12,.2f}")
print(f"  Worst    : ${min(final_values):>12,.2f}")
print(f"  Avg      : ${sum(final_values)/len(final_values):>12,.2f}")
print(f"  Loss runs: {loss_count}/{sim_cfg['trials']}")

# --- Example 2: random.randint() for synthetic dataset generation ---
raw_schema = '''
{
    "table": "synthetic_orders",
    "count": 12,
    "regions":   ["AMER","EMEA","APAC"],
    "products":  ["CoreDB","AnalytX","StreamIO","VaultAI"],
    "statuses":  ["pending","fulfilled","cancelled","refunded"]
}
'''

try:
    schema = json.loads(raw_schema)
except json.JSONDecodeError as e:
    schema = {"count": 0, "regions": [], "products": [], "statuses": []}

base_date = datetime(2024, 1, 1)

# randint(a, b) is inclusive on both ends — useful for ID ranges and offsets
synthetic_orders = [
    {
        "order_id":   f"ORD-{random.randint(10000, 99999)}",
        "customer_id": random.randint(1, 500),
        "region":     random.choice(schema["regions"]),
        "product":    random.choice(schema["products"]),
        "quantity":   random.randint(1, 50),
        "unit_price": round(random.uniform(29.99, 499.99), 2),
        "status":     random.choice(schema["statuses"]),
        # timedelta with random days offset generates realistic date spread
        "order_date": (base_date + timedelta(days=random.randint(0, 364))).strftime("%Y-%m-%d")
    }
    for _ in range(schema["count"])
]

# Aggregate revenue for fulfilled orders only
fulfilled_rev = round(sum(
    o["quantity"] * o["unit_price"]
    for o in synthetic_orders
    if o["status"] == "fulfilled"
), 2)

print(f"\nSynthetic Orders ({schema['count']} rows):")
for o in synthetic_orders[:4]:
    print(f"  {o['order_id']}  {o['product']:<10}  {o['region']}  {o['status']:<12}  ${o['quantity']*o['unit_price']:.2f}")
print(f"  ... (+{len(synthetic_orders)-4} more)")
print(f"  Fulfilled Revenue: ${fulfilled_rev:,.2f}")

# --- Example 3: random.choice() and random.choices() for sampling ---
raw_candidates = '''
{
    "pool": "A/B Test Cohort",
    "users": [
        {"id": 101, "name": "Alice",   "tier": "pro"},
        {"id": 102, "name": "Bob",     "tier": "free"},
        {"id": 103, "name": "Carol",   "tier": "pro"},
        {"id": 104, "name": "Dave",    "tier": "enterprise"},
        {"id": 105, "name": "Eve",     "tier": "free"},
        {"id": 106, "name": "Frank",   "tier": "enterprise"},
        {"id": 107, "name": "Grace",   "tier": "pro"},
        {"id": 108, "name": "Hank",    "tier": "free"}
    ],
    "weights": {"pro": 3, "enterprise": 5, "free": 1}
}
'''

try:
    cohort = json.loads(raw_candidates)
except json.JSONDecodeError as e:
    cohort = {"users": [], "weights": {}}

users   = cohort["users"]
weights_map = cohort["weights"]

# random.choice() — uniform single pick
spotlight = random.choice(users)
print(f"\nRandom spotlight user: {spotlight['name']} ({spotlight['tier']})")

# random.choices() — weighted sampling WITH replacement (higher-tier users more likely)
weight_list = [weights_map.get(u["tier"], 1) for u in users]
weighted_sample = random.choices(users, weights=weight_list, k=5)
print("Weighted sample (5):")
for u in weighted_sample:
    print(f"  {u['name']:<8} tier={u['tier']:<12} (weight={weights_map.get(u['tier'],1)})")

# --- Example 4: random.shuffle() for randomized pipelines and test fixtures ---
raw_pipeline = '''
{
    "name": "DataValidationSuite",
    "tasks": [
        {"id": "T1", "name": "null_check",      "priority": 1},
        {"id": "T2", "name": "type_validation", "priority": 1},
        {"id": "T3", "name": "range_check",     "priority": 2},
        {"id": "T4", "name": "uniqueness",      "priority": 2},
        {"id": "T5", "name": "referential",     "priority": 3}
    ]
}
'''

try:
    pipeline = json.loads(raw_pipeline)
except json.JSONDecodeError as e:
    pipeline = {"tasks": []}

# Separate high-priority tasks (must run first) from shuffleable remainder
fixed  = [t for t in pipeline["tasks"] if t["priority"] == 1]
others = [t for t in pipeline["tasks"] if t["priority"] > 1]

# shuffle() mutates in place — copy first to preserve original order
shuffled_others = others.copy()
random.shuffle(shuffled_others)

execution_order = fixed + shuffled_others
print(f"\nPipeline: {pipeline['name']}")
print("Execution order:")
for idx, task in enumerate(execution_order, 1):
    print(f"  {idx}. [{task['id']}] {task['name']}  (priority={task['priority']})")

# --- Example 5: random.sample() for stratified test splits, persisted to JSON ---
raw_dataset = '''
{
    "dataset": "iris_synthetic",
    "classes": ["setosa","versicolor","virginica"],
    "samples_per_class": 6
}
'''

try:
    ds_cfg = json.loads(raw_dataset)
except json.JSONDecodeError as e:
    ds_cfg = {"classes": [], "samples_per_class": 0}

# Generate synthetic labelled points, then stratified-sample for test split
all_samples = [
    {
        "id":    f"{cls[0].upper()}{i+1:02d}",
        "class": cls,
        # uniform() generates realistic float features
        "sepal_length": round(random.uniform(4.5, 7.9), 2),
        "sepal_width":  round(random.uniform(2.0, 4.5), 2),
        "petal_length": round(random.uniform(1.0, 6.9), 2),
        "petal_width":  round(random.uniform(0.1, 2.5), 2)
    }
    for cls in ds_cfg["classes"]
    for i in range(ds_cfg["samples_per_class"])
]

# Stratified split: sample() without replacement, 2 per class for test set
test_set = []
train_set = []
for cls in ds_cfg["classes"]:
    cls_samples = [s for s in all_samples if s["class"] == cls]
    # random.sample() guarantees no duplicates — critical for ML splits
    test_cls  = random.sample(cls_samples, k=2)
    train_cls = [s for s in cls_samples if s not in test_cls]
    test_set.extend(test_cls)
    train_set.extend(train_cls)

split_result = {
    "generated_at": datetime.now().isoformat(),
    "total_samples": len(all_samples),
    "train_size":    len(train_set),
    "test_size":     len(test_set),
    "train":         train_set,
    "test":          test_set,
    "simulation_trials": trials,
    "synthetic_orders":  synthetic_orders
}

out_path = os.path.join(OUTPUT_DIR, "random_module_results.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(split_result, f, indent=2)

print(f"\nDataset split → train={len(train_set)}  test={len(test_set)}")
print(f"Full results written → {out_path}")