# Final Project – Individual Component

**DS 4021** – Instructor: Javier Rasero; TAs: Kayla Kim & Yiqing Yang
**Due:** See Canvas
**Submission format:** One Jupyter notebook (`.ipynb`) to be uploaded to Canvas

## Individual Assignment

**General Description:** Each student must upload to Canvas a Jupyter notebook containing the models assigned to them, including well-annotated code and an explanation of the results. The same notebook must also be included in the group's GitHub repository (see the Rubric for the group component). Each student must submit their own notebook separately in order to receive an individual grade.

**Why am I doing this?** The goal of this assignment is to train and optimize machine learning methods you have learned throughout the course to help your group select the best model for deployment. Think of this as the stage of a real-world project in which different team members develop and optimize predictive models before selecting one for deployment. Using the same dataset and research question that your group selected previously, you will train, optimize, and validate the predictive models assigned to you.

**What will I do?** You will complete the model training and optimization part of the project individually. Each student will work with the same training set and use the agreed-upon metrics so the group can compare the models later. You must NOT use the reporting set you have already put aside during this stage.

**How will this be graded?** This individual assignment is worth 100 points: model implementation, training, and optimization (60 points); presentation and interpretation of the results (30 points); and notebook documentation and reproducibility (10 points). This component is worth 50% of your final project grade.

You will be graded on the work you complete for your chosen model(s), not on the work of your teammates. All individual modeling assignments are graded using the same criteria.

Each student is responsible for completing a different modeling assignment within their group. The distribution of modeling assignments must be clearly specified in the group's `README.md` file (see the Rubric for the group component).

> **IMPORTANT:**
> If a student submits a modeling assignment that does not match the one assigned to them in the group's `README.md` file, they will receive a 50-point deduction from their individual project grade (out of 100 points).
>
> If two or more students from the same group submit the same modeling assignment and the `README.md` file does not clearly establish their individual responsibilities, each student involved will receive the same 50-point deduction.
>
> The penalty will be applied only once per student, and the individual project grade cannot fall below zero.
>
> This penalty will apply to the final submissions only. Students may change their modeling assignments before the deadline, provided that all required models for their group size remain covered and the group's `README.md` file is updated accordingly.

## Rubric

### Model assignments

**For groups of THREE students**, each group member must complete ONE of the following assignments:

- **Student 1:** A penalized (Ridge, Lasso or ElasticNet) linear model (Linear Regression or Logistic Regression, as appropriate) AND a Support Vector Machine.
- **Student 2:** TWO ensemble methods: one Bagging-type model (e.g., Random Forest) AND one Boosting-type model (e.g., Gradient Boosting).
- **Student 3:** ONE neural network implemented and trained in PyTorch. Using scikit-learn for this will not be accepted and will result in a score of zero for the model training and optimization portion (0 out of 60 points; see below).

**For groups of TWO students**, the modeling assignments are as follows:

- **Student 1:** A penalized (Ridge, Lasso or ElasticNet) linear model (Linear Regression or Logistic Regression, as appropriate) OR a Support Vector Machine; AND one Bagging-type model (e.g., Random Forest) OR one Boosting-type model (e.g., Gradient Boosting).
- **Student 2:** ONE neural network implemented and trained in PyTorch. Using scikit-learn for this will not be accepted and will result in a score of zero for the model training and optimization portion (0 out of 60 points; see below).

For groups of two, Student 1 must clearly specify their two selected models at the beginning of their notebook.

> **IMPORTANT:** Each group member must complete a different modeling assignment. Group members must coordinate their responsibilities before starting the project. The assignment of models to group members must be clearly specified in the group's `README.md` file and must match the individual notebooks submitted to Canvas.

### Formatting

- Upload ONE Jupyter notebook (`.ipynb`) directly to Canvas. Students assigned two models must include both models in the same notebook.
- Include your name, group, and assigned model(s) at the beginning of the notebook.
- The notebook uploaded to Canvas must be the same version as the one included in the group repository.
- **IMPORTANT:** Also place the final version of your notebook in the `NOTEBOOKS` folder of the shared group GitHub repository (see the Rubric for the group component).

### Model training and optimization (60 points)

To get all points here, you will need to:

- Complete the training and optimization of ALL models assigned to you.
- Use cross-validation to tune your models and try different hyperparameter combinations.
- Embed preprocessing inside the cross-validation to avoid data leakage. You may accomplish this using pipelines or equivalent procedures.
- For the neural network, you must use PyTorch for all aspects of its implementation, training, and prediction (architecture, training procedure, cost function, optimizer, etc.). Explain the relevant training choices. *N.B.* Using scikit-learn to implement, train, or generate predictions with the neural network will not be accepted and will result in a score of zero for this portion (0 out of 60 points).
- Clearly describe how you selected the optimal hyperparameters for each model.

> **REMEMBER:** You must not use the reporting set you put aside in the prerequisite Final Project assignment for training or optimization. Using the reporting set for any of these purposes will result in a 60-point deduction from your individual assignment grade (out of 100 points).

### Presentation of results (30 points)

To get all points here, you will need to:

- Report the cross-validated performance for each of your assigned models and the explored hyperparameters.
- Use more than one appropriate performance metric, e.g. Accuracy and confusion matrix for classification, or Coefficient of determination and Mean Square Error for regression.
- Present the results in clear, well-labeled tables or figures. For assignments with two models, compare the results of both models.
- Briefly discuss your findings, differences in performance, and any relevant limitations.
- Provide results your group can use to compare all the models in the final report.

You will be graded on how well the models are evaluated and the results are presented, not on whether they achieve the highest predictive performance. For example, using accuracy for a regression task is wrong and will be heavily penalized.

### Documentation (10 points)

To get all points here, the following conditions must be met:

- Notebooks must run top-to-bottom without errors.
- Code must be accompanied by explanatory text. Use Markdown headers to separate the modeling steps.
- Figures must be readable and well labeled.
- Random seeds must be set whenever possible for reproducibility. Include any packages or instructions necessary to run the notebook.
- Include a short section describing the tasks you completed and the main findings. No separate individual PDF report is required for this submission.
- Identify the data and any supporting files required to run the notebook; these should be available from the group repository or an accessible link.
