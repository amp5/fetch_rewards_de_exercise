# fetch_rewards_de_exercise
Coding challenge for Fetch Rewards


Included in this git repo is a program that takes as inputs two texts and uses a metric to determine how similar they are using a 0.0 - 1.0 scale. A score of 0 meaning no similarity and a score of 1 meaning the two texts are exactly the same. The program is built using Python, Flask and Docker. 

# Getting Started
 To run this program:
 
 - Create a folder to store this repo locally 
 ``` mkdir applicant_program```
 
 - Clone this GitHub repo:
 ``` git clone https://github.com/amp5/fetch_rewards_de_exercise.git ```

 - Determine if you want to run this locally using just Flask or want to run this using Docker Hub

 ## Run Locally

 ## Run via Docker






## Determining the metric for similarity
Given that the coding exercise directions talked only about how many words both texts had in common as the definition for similarity and doesn't get into the specifics on how this metric might be used, this program's calculation does not factor in the following:

- The difference between upper and lower case text. (i.e "hello world" vs "Hello World" have 2 words in common)
- sentiment between texts (i.e. "I love pizza" vs "I hate pizza" both have 2/3 words in common. The difference between love and hate here is not a factor in similarity despite the fact that this would certainly be something to account for in production as these two texts would be on opposite spectrums of sentiment.)
- punctuation between texts (i.e. "Have a great day?" vs "Have a great day!" both have 4 words in common. The difference between punctuation is often to convey certain emotions or sentiment and in the case where this program is built out further to include most frequently used non-filler words like 'a', 'the' etc. punctuation doesn't povide much useful information in terms of potential trends among the text inputs.)
- order of words between texts (i.e. "Sally bought icecream for Rick" vs "Rick bought icecream for Sally" have 5/5 words in common but the meaning behind the texts is not the same. The same person did not buy icrecream for the other person) Thus this program is not implementing a sequence-based approach



To calculate similarity this program ulitizes a token-based approach to find similar tokens in both sets. Two common algorithms for this approach are the Jaccard index and the Sorensen-Dice. I will be using the Jaccard index which finds the number of common tokens and divides it by the total number of unique tokens. The Sorensen-Dice algorithm is similar but often overestimates the similarity between two strings.

Below is the formula for the Jaccard index as referenced from this [article](https://itnext.io/string-similarity-the-basic-know-your-algorithms-guide-3de3d7346227):


![Jaccard Index](https://user-images.githubusercontent.com/5368361/115926550-df36d000-a437-11eb-86a8-25bea8dfbb0d.png)

A more robust, perhaps future refactorization of this metric could include the removal of stop words (i.e. "I", "or", "the", "to") as well as stemming the inputs (i.e. "buy" and "buy(ing)" would be counted as buy).

## Potential Use Case
- Identifying for example duplicate or fake reviews for Fetch Rewards on Google Play or the iTunes store. 
- Identifying similar receipts (this step would most likely be post image processing). For example identifying clothing receipts compared to grocery receipts.


