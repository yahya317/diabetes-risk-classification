# Final Project – Group Component

**DS 4021** – Instructor: Javier Rasero; TAs: Kayla Kim & Yiqing Yang
**Due:** See Canvas
**Submission format:** Link to the final commit of the group's GitHub project repository, submitted through Canvas.

## Group Assignment

**General Description:** Submit to Canvas a link to the final GitHub commit of your group's project. This commit must be from the same repository created for the prerequisite assignment, which will contain all materials related to your final project, including the descriptive analysis, the individual modeling notebooks from all group members, the final reporting-set evaluation, documentation, figures, and a final report summarizing the results.

> **IMPORTANT:** Each group must submit to Canvas a link to the final GitHub commit of their project before the deadline. We will grade the repository as it existed at that specific commit. Any changes made after the submitted commit will not be considered for grading. Submitting only the GitHub repository URL, rather than a specific commit link, is not a valid submission and will result in a score of zero for the Group Component (0 out of 100 points).

**Why am I doing this?** The goal here is to put into practice everything you have learned throughout this course in a comprehensive machine learning project that resembles a real-world application. Think of this as a Kaggle competition or a machine learning project carried out by a team within a company. Using the same dataset and research question that you selected previously, your group will perform exploratory visualization, descriptive statistics, compare the models trained and optimized individually, and evaluate the selected best model on the held-out reporting set.

**What will we do?** Your group will complete the descriptive analysis and final reporting-set evaluation, bring together the modeling notebooks completed by each student, and write a concise report presenting the main results and findings. Work should be divided among team members.

**How will this be graded?** The group assignment is worth 100 points. The Descriptive Analysis Notebook is worth 20 points, the Final Reporting-Set Evaluation Notebook is worth 20 points, and the final report is worth 60 points. This component is worth 50% of your final project grade.

See the table below for a detailed description of where the points come from.

> **IMPORTANT:**
> The group's GitHub repository must include all individual modeling notebooks (see the Rubric for the individual component of the project), in addition to the descriptive analysis and final reporting-set evaluation notebooks.
>
> Each group member is responsible for uploading their individual modeling notebook to the shared repository. However, making sure that the repository contains all required notebooks is a shared responsibility of the entire group.
>
> For each missing individual modeling notebook, 20 points will be deducted from the group assignment grade (out of 100 points), up to a maximum deduction of 40 points.
>
> This penalty applies to all group members, regardless of which student was responsible for the missing notebook.
>
> Any individual modeling notebook missing from the repository at the submitted commit will be considered missing for grading. The corresponding 20-point penalty will still apply, even if the notebook is added afterward.

## Rubric

### Formatting

- One GitHub repository (submit the final commit link via Canvas).

The top level page of the repository should contain:

- A `README.md` file (which auto displays)
- A `NOTEBOOKS` folder
- A `Data` folder
- An `OUTPUT` folder
- A `final_report.pdf` file

### README.md

**Goal:** The README helps others quickly understand your project. Keep it short, clear, and written for someone who has never seen your files before.

- Use markdown headers to divide content.
- Make an H2 (`##`) section explaining the contents of the repository.

It must include the following three sections:

- **Section 1: Software and platform.** List the Python version, Jupyter notebooks, packages (pandas, numpy, scikit-learn, matplotlib, seaborn, PyTorch), and operating system.
- **Section 2: A map of your documentation.** Provide a folder tree listing the files stored in each folder or subfolder.
- **Section 3: Group Member Responsibilities.** Include a table listing each group member and their assigned modeling task. Each group member must be assigned a different modeling task, following the instructions specified in the Individual Component rubric for groups of two or three students. The assignments listed here MUST match the individual notebooks submitted to Canvas.

### NOTEBOOKS folder

**Goal:** This folder contains all the Jupyter notebooks for your project.

These are the required notebooks you will need to upload:

1. **Descriptive Analysis Notebook (20 points):**
   - Exploratory visualizations
   - Summary statistics
   - *Note:* You may use the training set for this descriptive analysis.
2. **The notebooks from the individual component part** (included in repository; graded individually – see Rubric for the individual component):
   - All these notebooks must be included in this folder. Each student must upload their own notebook to Canvas separately for the individual grade.
3. **Final Reporting-Set Evaluation Notebook (20 points):**
   - After comparing the performance of the optimized models using their cross-validation results, select the best model (including its optimal hyperparameters).
   - Fit the selected model to the entire training set.
   - Evaluate it on the reporting set you had initially put aside and report the final results.
   - **REMEMBER:** Here is where you must use the reporting set you put aside in the prerequisite Final Project assignment. Not evaluating on the correct reporting set will result in ZERO points for this part.

### Notebook Requirements

- Cross-validation results and hyperparameter choices must be clearly documented for model comparison.
- Do not use the reporting set for model selection, hyperparameter optimization, or fitting preprocessing procedures. Avoid data leakage.
- Assess and report the final model's performance using more than one metric.
- The group notebooks must run top-to-bottom without errors.
- Code must be accompanied by explanatory text; figures must be readable and well labeled.
- Random seeds must be set whenever possible for reproducibility.

### Data folder

- This is the same folder where you originally uploaded the reporting set.
- For the final project, this folder should also contain the training set.
- If any data are too large for GitHub, upload them to a platform such as Google Drive and include a link with appropriate download permissions.

### OUTPUT folder

- **Goal:** Store all outputs generated during the project (figures, tables, etc.).
- *N.B.* It is OK to leave this folder blank if all outputs are inline in the notebooks.

### final_report.pdf (60 points)

- **Goal:** To summarize everything into a final report file.
- A PDF file 1 or 2 pages long.

**Structure**

- **One introductory paragraph with:**
  - **Research question.** You may reinstate or refine the same research question you used for the prerequisite document. Remember that your research question needs to be testable. For example, something like: "which factors contribute most to...", "which features are the most predictive…" might now be directly addressable for some models (e.g. Neural Networks or SVM with non-linear Kernel). A good and testable research question could just be: "Can we successfully predict [SOMETHING]?" "What model best predicts [SOMETHING]?"
  - **Motivation.**
- **One or two methods paragraphs with:**
  - Dataset description and summary of any data cleaning/curation.
  - Outline of each model used, including its preprocessing steps.
  - Cross-validation strategy and metrics used to assess model performance.
- **One or two results paragraphs with:**
  - Key findings and model results.
  - One table showing the cross-validated performance of each best model.
  - The performance of the selected best model on the held-out reporting set.
- **One or two discussion paragraphs with:**
  - Interpretation of results.
  - Why some models may perform better than others.
  - Limitations of the project.

### Group coordination

- Each student must add their completed individual notebook to the group GitHub repository and separately upload the same notebook to Canvas.
- The group should use the same training data and agreed-upon metric to compare the models fairly.
- The group grade is based on the group components listed above. Individual model implementation and optimization are graded separately from the notebook uploaded to Canvas.
- If a model notebook or its results are unavailable, explain the missing contribution rather than reporting results that were not obtained. The shared analyses will be graded based on what the group submitted.
