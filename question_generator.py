import random


QUESTION_BANK = {

    "python": [
        "What are Python decorators?",
        "Explain generators in Python.",
        "Difference between List and Tuple.",
        "Explain OOP in Python.",
        "What are lambda functions?",
        "What is list comprehension?",
        "Explain exception handling.",
        "What is the GIL?",
        "Difference between deepcopy and shallow copy.",
        "Explain *args and **kwargs."
    ],

    "java": [
        "Explain JVM.",
        "Difference between JDK and JRE.",
        "What is inheritance?",
        "What is polymorphism?",
        "Explain multithreading.",
        "What is an interface?",
        "Difference between ArrayList and LinkedList.",
        "Explain Exception Handling.",
        "What is Garbage Collection?",
        "Explain the Collections Framework."
    ],

    "sql": [
        "Explain INNER JOIN.",
        "Difference between DELETE and TRUNCATE.",
        "What is a Primary Key?",
        "Difference between WHERE and HAVING.",
        "Explain Normalization.",
        "What are indexes?",
        "What is a stored procedure?",
        "Difference between UNION and UNION ALL.",
        "Explain GROUP BY.",
        "What is a Foreign Key?"
    ],

    "aws": [
        "What is Amazon EC2?",
        "Difference between EC2 and Lambda.",
        "Explain Amazon S3.",
        "What is IAM?",
        "Explain VPC.",
        "Difference between EBS and S3.",
        "What is CloudWatch?",
        "Explain Auto Scaling.",
        "What is RDS?",
        "Explain API Gateway."
    ],

    "machine learning": [
        "What is supervised learning?",
        "Difference between Classification and Regression.",
        "Explain Overfitting.",
        "What is Cross Validation?",
        "Explain Random Forest.",
        "What is Gradient Descent?",
        "Difference between Bagging and Boosting.",
        "Explain Feature Engineering.",
        "What is Precision and Recall?",
        "What is F1 Score?"
    ],

    "deep learning": [
        "What is CNN?",
        "Explain Transfer Learning.",
        "Difference between CNN and RNN.",
        "What is Backpropagation?",
        "Explain Activation Functions.",
        "What is Batch Normalization?",
        "Explain Dropout.",
        "What is an Epoch?",
        "Difference between TensorFlow and PyTorch.",
        "Explain LSTM."
    ],

    "opencv": [
        "What is OpenCV?",
        "Explain image thresholding.",
        "What is edge detection?",
        "Difference between erosion and dilation.",
        "Explain contour detection.",
        "How does face detection work?",
        "What is image segmentation?",
        "Explain image filtering.",
        "What is histogram equalization?",
        "Explain object tracking."
    ],

    "html": [
        "What is Semantic HTML?",
        "Difference between HTML and HTML5?",
        "Explain Forms.",
        "What are meta tags?",
        "Difference between id and class?"
    ],

    "css": [
        "Explain Flexbox.",
        "Difference between Grid and Flexbox.",
        "What is CSS Specificity?",
        "Explain Media Queries.",
        "What is Position Absolute?"
    ],

    "javascript": [
        "Explain Closures.",
        "Difference between var, let and const.",
        "What is Hoisting?",
        "Explain Promises.",
        "Difference between == and ===."
    ]

}


def generate_questions(skills):

    interview_questions = []

    for skill in skills:

        if skill in QUESTION_BANK:

            interview_questions.extend(
                random.sample(
                    QUESTION_BANK[skill],
                    min(5, len(QUESTION_BANK[skill]))
                )
            )

    if not interview_questions:

        interview_questions = [
            "Tell me about yourself.",
            "Why should we hire you?",
            "What are your strengths?",
            "Describe your biggest project.",
            "Where do you see yourself in five years?"
        ]

    random.shuffle(interview_questions)

    return interview_questions