import cohere
from conf import API_KEY

co = cohere.Client(API_KEY)

response = co.generate(
  model='command-xlarge-nightly',
  prompt='How to create startup?',
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
