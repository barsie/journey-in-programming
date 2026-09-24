# Learning and Capstone Scaffold for journey-in-programming

A repository that organizes learning paths, technology experiments, and capstone work in one place.

## Folder structure

```text
.
├── Learning/
│   ├── CodingAzure/
│   ├── CodingJava/
│   ├── CodingPython/
│   ├── CodingTypeScript/
│   ├── Databases/
│   ├── DSA/
│   ├── MachineLearning/
│   ├── NetworkAnalysis/
│   ├── ProgrammingAssignments/
│   ├── React/
│   ├── ShellScripting/
│   ├── StatisticalAnalysis/
│   └── VanillaJavaScript/
└── Capstone/
    ├── Projects/
    └── Submodules/
```

Local `.gitignore` files may be added inside learning or project folders when a specific workspace needs tool-specific artifact exclusions.

## Naming convention

- `Learning/` contains domain-specific folders for practice, notes, and small experiments.
- `Capstone/Projects/` contains larger project work.
- `Capstone/Submodules/` is reserved for linked repositories or nested project imports when needed.
- Short, capitalized section names are used at the top level, and learning folders use a consistent PascalCase-style naming pattern, with short acronyms such as `DSA` allowed where they are clearer.
- `ProgrammingAssignments` is the intentional cross-topic exception within `Learning/` for coursework that spans more than one domain or technology.

## Technology mapping

- Java: `Learning/CodingJava`
- Python: `Learning/CodingPython`
- TypeScript: `Learning/CodingTypeScript`
- JavaScript: `Learning/VanillaJavaScript`
- React: `Learning/React`
- Shell: `Learning/ShellScripting`
- Azure and cloud exercises: `Learning/CodingAzure`
- Data structures and algorithms: `Learning/DSA`
- Machine learning experiments: `Learning/MachineLearning`
- Network analysis work: `Learning/NetworkAnalysis`
- SQL and NoSQL: `Learning/Databases`
- R and statistics work: `Learning/StatisticalAnalysis`
- Cross-topic coursework and mixed assignments: `Learning/ProgrammingAssignments`

## Placement rules

- A shared assignment is a single coursework deliverable that intentionally spans multiple technologies or topics.
- Keep assignment code, JSON, sample data, and configuration files together with that shared assignment.
- Single-topic exercises should stay in their corresponding learning folder.
- Project deliverables should live in `Capstone/Projects/`.
- Linked repositories or nested imports should go in `Capstone/Submodules/`.
