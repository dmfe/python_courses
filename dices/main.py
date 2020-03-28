from experiment import Experiment

ex = Experiment(lambda sum : sum == 4, 100)
ex.run()
print(f'Frequency probability: {ex.get_probabily()}')
