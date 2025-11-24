import pysam
from typing import List
from sklearn.ensemble import HistGradientBoostingClassifier
import numpy as np
import pandas as pd

class GeoPredictor:
    def __init__(self, model: HistGradientBoostingClassifier, input_features: List[tuple]):
        self.model = model
        self.input_features = input_features

    def predict(self, vcf_file: dict) -> dict:
        variants = self.get_variants_from_vcf(vcf_file)
        input_data = [variants.get(feat, np.nan) for feat in self.input_features]
        probs = self.model.predict_proba([input_data])[0]
        tab = pd.DataFrame(zip(self.model.classes_,probs))
        tab.columns = ['Region','Probability']
        return tab.sort_values(by='Probability', ascending=False)

    def get_variants_from_vcf(self, filename):
        vcf = pysam.VariantFile(filename)
        variants = {}
        for var in vcf:
            key = (var.chrom, var.pos,var.alts[0])
            if key in self.input_features:
                variants[key] = var.samples[0]['GT'][0]
        return variants