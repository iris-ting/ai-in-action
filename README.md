## Inspiration

Modern software testing is time-consuming, and writing good test cases often falls behind rapid development cycles. We were inspired to leverage AI to **automatically generate high-quality test cases** based on user code commits — helping developers move faster while maintaining code integrity. Our goal was to build a **seamless, CI-integrated AI test assistant** that generates, validates, and logs test scripts based on real-time code changes.

---

## What It Does

**Gen Test** is an AI-powered test generation system that:

- Provides a **web interface** for user login via Firebase
- Tracks **code changes in GitLab** through `.gitlab-ci.yml`
- Automatically sends modified code files to **Vertex AI (Gemini)** for test generation
- Validates the AI-generated test code and stores metadata in **Firestore**
- Displays test results and code output in the **frontend dashboard**

---

## How We Built It

- **Frontend**: A simple web UI that handles user login (via Firebase) and shows test results stored in Firestore.
- **Backend**: A Flask microservice deployed on **Google App Engine** that:
  - Sends customized prompts to **Vertex AI (Gemini)** to generate test scripts
  - Validates returned code with Python AST parsing
  - Stores results (including success flag and test script) in **Firestore**
- **CI/CD Integration**:
  - `.gitlab-ci.yml` runs `get_difference.py` to identify modified Python files
  - Modified files are sent to our Flask endpoint for test generation and validation
- **Database**: **Firestore** stores each test record with metadata including:
  - Filename
  - Test code
  - Validation status
  - User role
  - Test Focus
  - Test Environment
  - Timestamp

---

## Challenges We Ran Into

- Stabilizing interactions with **Vertex AI**, particularly with respect to prompt formatting and auth
- Implementing **custom user metadata and access control** via Firebase and Firestore
- Configuring **GitLab CI/CD pipelines** to trigger our service smoothly
- Ensuring that generated test code was **not only valid Python, but semantically correct and runnable**
- Designing a prompt system that could dynamically adapt to user-specific strategies like "edge case coverage" or "robust input validation"


---

## Accomplishments That We're Proud Of

- A fully functional **end-to-end pipeline** from code commit to validated test generation and web display
- Seamless integration between **GitLab, Vertex AI, Firebase**, and Flask
- Custom prompts that adapt to **user roles** and other metadata
- 100% of test scripts from AI passed syntax and unittest-style validation

---

## What We Learned

- Prompt engineering is critical — phrasing impacts AI behavior significantly
- Vertex AI’s Gemini models are reliable for generating structured Python code, given the right context
- CI/CD workflows can become **AI-enhanced** with minimal effort when done right
- Firebase + Firestore are perfect for combining real-time updates with document-based querying

---

## What's Next for AI in Action

- Add support for **multi-language test generation** (e.g., JavaScript, Java, Go)
- Allow users to define **test strategies** like boundary testing, fuzzing, or contract-based tests
- Track prompt effectiveness using **validation feedback loops**
- Package our system as a **DevOps-ready open-source toolkit**
- Expand compatibility beyond GitLab (e.g., GitHub Actions, Bitbucket Pipelines)
