Competition Name: Anadolu Hayat Emeklilik Datathon 2024

Competition Link: https://www.kaggle.com/competitions/anadolu-hayat-emeklilik-datathon-2024/leaderboard?

Result: 12th/185

----------------------------------------------------

[TR]

Problem: Yaklaşık 853000 müşterinin gelecek aylarda ürün alıp almayacağı, alırsa hangi ürünü alacağının tahmin edilmesi isteniyor. 7 sınıflı bir multiclass classification.

Zorluklar:

-Aşırı dengesiz bir veri seti. Setin yaklaşık %97.7'si ürün almayan müşterilerden oluşmakta.

-Hedef metrik custom bir f1 metriği. Sette az görülen sınıfların ağırlıkları görülme oranlarıyla ters orantılı. Yani ürün alan müşterilerin iyi tahmin edilmesi gerekiyor.

Yaklaşımımız: 

Sorunu çözmek için 2 aşamalı bir çözüm sunduk. ilk önce müşterinin ürün alıp almayacağını tahmin ediyoruz (binary classification). Eğer ürün almıyorsa UA sınıfı olarak tahmin ediyoruz. Eğer ürün alır şeklinde tahmin edersek hangi ürünü alacağını tahmin etmeye çalışıyoruz (multiclass classification)

Geliştirilebilecek yönler:

-Daha çok feature engineering yapılabilir.

-Feature selection yapılmalı.

-Manuel modeller HPO yapıldıktan sonra AutoGluon ile ensemble edilebilir.

-----------------------------------------------------------

[EN]

Problem: The task is to predict whether approximately 853,000 customers will purchase a product in the coming months and, if so, which product they will buy. This is a 7-class multiclass classification problem.

Challenges:

-Highly imbalanced dataset. About 97.7% of the dataset consists of customers who do not purchase any products.

-The target metric is a custom F1 metric. The weights of the less frequent classes are inversely proportional to their occurrence rate. Therefore, it is important to accurately predict the customers who do purchase products.

Our Approach:

To solve the problem, we proposed a two-stage solution. First, we predict whether the customer will purchase a product (binary classification). If they are not predicted to purchase a product, they are classified as the "UA" class. If they are predicted to purchase a product, we then try to predict which product they will buy (multiclass classification).

Areas for Improvement:

-More feature engineering can be done.

-Feature selection should be performed.

-Manual models can be trained with HPO and then ensembled with AutoGluon.

