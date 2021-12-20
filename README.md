# text_gcn.pytorch

This project implements ["Graph Convolutional Networks for Text Classification. Yao et al. AAAI2019."](https://arxiv.org/abs/1809.05679) in PyTorch.

This implementation modified from https://github.com/iworldtong/text_gcn.pytorch


## Require

* Python 3.6
* PyTorch 1.0

## Running training and evaluation

1. `cd ./preprocess`
2. Run `python remove_words.py <dataset>`
3. Run `python build_graph.py <dataset>`
4. `cd ..`
5. Run `python train.py <dataset>`
6. Replace `<dataset>` with `P1`, `P2`

## Visualization

Check P1_gcn_doc_test.pdf and P2_gcn_doc_test.pdf
