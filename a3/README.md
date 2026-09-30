# Assignment 3
* Brief [instructions and installation] for [Assignment3].
* For detailed executions, see [assignment3.ipynb].

## Note
* Implemented algorithms:
  * [x] Reinforcement Learning from Human Preferences (RLHF)
  * [x] Direct Preference Optimization (DPO)

## Result
### 1 Reward Engineering
* Learning curves  
  <img src="results/hopper.png" width="40%" />
* Evaluation rollouts  
  with early termination  
  <img src="results/1-wet_eval_ep2.gif" width="25%" />
  <img src="results/1-wet_eval_ep9.gif" width="25%" /><br>
  without early termination  
  <img src="results/1-woet_eval_ep1.gif" width="25%" />
  <img src="results/1-woet_eval_ep8.gif" width="25%" />
### 2 Learning from Preferences
* Learning curves  
  <img src="results/hopper_rlhf.png" width="40%" />
* Evaluation rollouts  
  <img src="results/2-eval_ep2.gif" width="25%" />
  <img src="results/2-eval_ep6.gif" width="25%" />
### 3 Direct Preference Optimization
* Learning curves  
  <img src="results/hopper_dpo.png" width="40%" />
* Evaluation rollouts  
  SFT vs. DPO  
  <img src="results/3-eval_ep3.gif" width="50%" />  
  <img src="results/3-eval_ep7.gif" width="50%" />

## Reference
* [Deep Reinforcement Learning from Human Preferences], P Christiano *et al.*
* [Direct Preference Optimization: Your Language Model is Secretly a Reward Model], R Rafailov *et al.*



[instructions and installation]: README_.md
[Assignment3]: https://web.stanford.edu/class/cs234/assignments/a3/hw3_questions.pdf
[assignment3.ipynb]: assignment3.ipynb
[Deep Reinforcement Learning from Human Preferences]: https://arxiv.org/abs/1706.03741
[Direct Preference Optimization: Your Language Model is Secretly a Reward Model]: https://arxiv.org/abs/2305.18290

