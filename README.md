---

# Pokémon Type Prediction

This project predicts a Pokémon’s type(s) using a combination of base stat distributions and Pokédex text descriptions. It approaches the task as a **multi-label classification problem** and uses a **Recurrent Neural Network (RNN)** with **TF-IDF vectorization** and **statistical feature engineering**.

## Project Structure
- **Dataset**: Kaggle dataset — "Pokédex for All 1025 Pokémon with Text Description."
- **Baseline**: Random assignment of types.
- **Model**: RNN combining normalized stats and TF-IDF vectors.
- **Evaluation Metrics**: Top-2 Accuracy, Macro/Weighted F1-score.

## Results
- **Top-2 Validation Accuracy**: ~49.76%
- **Macro F1 Score**: ~0.3395
- **Weighted F1 Score**: ~0.3374

## Key Techniques
- Text preprocessing: stopword removal, lemmatization, TF-IDF.
- Stat feature normalization and feature engineering.
- RNN model with dropout, L2 regularization, and early stopping.

## Future Improvements
- Experimenting with Transformers or feedforward neural networks.
- Using context-aware embeddings like BERT.
- Addressing class imbalance through resampling or class-weighted loss.

## Authors
- Arveen Adap
- Rikki Casupanan
- Marcus Tubera

---

# 🛠 How to Run
1. Install required Python libraries: `numpy`, `pandas`, `scikit-learn`, `tensorflow`, `nltk`.
2. Open and run `RNN.ipynb` notebook.
3. Dataset should be placed in the working directory or correctly referenced inside the notebook.

---
