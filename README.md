# fetch_rewards_de_exercise
Coding challenge for Fetch Rewards

### Determining the metric for similarity
Given that the coding exercise directions talked only about how many words both texts had in common as the definition for similarity and doesn't get into the specifics on how this metric might be used, this program's calculation does not factor in the following:

- sentiment between texts (i.e. "I love pizza" vs "I hate pizza" both have 2/3 words in common. The difference between love and hate here is not a factor in similarity despite the fact that this would certainly be something to account for in production as these two texts would be on opposite spectrums of sentiment.)
- punctuation between texts (i.e. "Have a great day?" vs "Have a great day!" both have 4 words in common. The difference between punctuation is often to convey certain emotions or sentiment and in the case where this program is built out further to include most frequently used non-filler words like 'a', 'the' etc. punctuation doesn't povide much useful information in terms of potential trends among the text inputs.)
- order of words between texts (i.e. "Sally bought icecream for Rick" vs "Rick bought icecream for Sally" have 5/5 words in common but the meaning behind the texts is not the same. The same person did not buy icrecream for the other person) Thus this program is not implementing a sequence-based approach


To calculate similarity this program ulitizes a token-based approach to find similar tokens in both sets. Two common algorithms for this approach are the Jaccard index and the Sorensen-Dice. I will be using the Jaccard index which finds the number of common tokens and divides it by the total number of unique tokens. The Sorensen-Dice algorithm is similar but often overestimates the similarity between two strings.

Below is the formula for the Jaccard index as referenced from this [article](https://itnext.io/string-similarity-the-basic-know-your-algorithms-guide-3de3d7346227):





I've chosen to create a simple caluclation as well as detail a more robust calculation below. The simple calculation is merely counting each distinct word in each text and comparing the two to see how many words and word frequencies overlap. A more robust calculation that might be used to better understand patterns in the data would factor out common stop words (i.e. "I", "or", "the", "to"), potentially stem words (i.e. "buy" and "buy(ing)" would be counted as buy) as well as either removing numbers or replacing numbers with string versions of numbers. 