# Transformer_for_abstract_summarization

the Transformer model from https://github.com/Kyubyong/transformer

### the dataset is LCSTS ,from http://icrc.hitsz.edu.cn/Article/show/139.html 



## STEP 1. how to train
    Run the following command:

        python train.py
        
    Check hparams.py to see which parameters are possible. For example,

        python train.py --logdir myLog --batch_size 256 --dropout_rate 0.5




## STEP 2. how to test
    Run the following command:

        python test.py --ckpt log/1/iwslt2016_E17L2.78-26078 (OR yourCkptFile OR yourCkptFileDirectory)
