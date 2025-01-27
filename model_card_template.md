# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
User Developing: Erica Greene
Model Date: 01/26/2025
Model Version: 1.0
Model Type: RandomForest Classifier

## Intended Use
Determine if a person makes over 50k a year based on comparison of following characteristics:
    - "workclass",
    - "education",
    - "marital-status",
    - "occupation",
    - "relationship",
    - "race",
    - "sex",
    - "native-country"


## Training Data
Used 80% of the original dataset for the training purposes.


## Evaluation Data
Used 20% of the original dataset for evaluation purposes.

## Metrics
Evaluated three metrics:
    -f1 score (0.6789)
    -precision score (0.7376)
    -recall score (0.6288)

## Ethical Considerations
The dataset may be flawed because we did not consider any outliers.

## Caveats and Recommendations
We may need to consider the age of the data itself because in today's world of 2025, education does
not guarantee a higher paying job.