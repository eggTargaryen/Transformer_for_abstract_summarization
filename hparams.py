import argparse

class Hparams:
    parser = argparse.ArgumentParser()

    # prepro
    parser.add_argument('--vocab_size', default=12000, type=int)

    # train
    ## files
    parser.add_argument('--train1', default='lcsts_data/train.src',
                             help="german training segmented data")
    parser.add_argument('--train2', default='lcsts_data/train.tgt',
                             help="english training segmented data")
    parser.add_argument('--eval1', default='lcsts_data/test.src',
                             help="german evaluation segmented data")
    parser.add_argument('--eval2', default='lcsts_data/test.tgt',
                             help="english evaluation segmented data")
    parser.add_argument('--eval3', default='lcsts_data/test.tgt',
                             help="english evaluation unsegmented data")

    ## vocabulary
    parser.add_argument('--vocab', default='lcsts_data/vocab.txt',
                        help="vocabulary file path")

    # training scheme
    parser.add_argument('--batch_size', default=128, type=int)
    parser.add_argument('--eval_batch_size', default=128, type=int)

    parser.add_argument('--lr', default=0.0003, type=float, help="learning rate")
    parser.add_argument('--warmup_steps', default=4000, type=int)
    parser.add_argument('--logdir', default="log/1", help="log directory")
    parser.add_argument('--num_epochs', default=20, type=int)
    parser.add_argument('--evaldir', default="eval/1", help="evaluation dir")

    # model
    parser.add_argument('--d_model', default=512, type=int,
                        help="hidden dimension of encoder/decoder")
    parser.add_argument('--d_ff', default=2048, type=int,
                        help="hidden dimension of feedforward layer")
    parser.add_argument('--num_blocks', default=6, type=int,
                        help="number of encoder/decoder blocks")
    parser.add_argument('--num_heads', default=8, type=int,
                        help="number of attention heads")
    parser.add_argument('--maxlen1', default=150, type=int,
                        help="maximum length of a source sequence")
    parser.add_argument('--maxlen2', default=40, type=int,
                        help="maximum length of a target sequence")
    parser.add_argument('--dropout_rate', default=0.3, type=float)
    parser.add_argument('--smoothing', default=0.1, type=float,
                        help="label smoothing rate")

    # test
    parser.add_argument('--test1', default='lcsts_data/test.src',
                        help="german test segmented data")
    parser.add_argument('--test2', default='lcsts_data/test.tgt',
                        help="english test data")
    parser.add_argument('--ckpt', help="checkpoint file path")
    parser.add_argument('--test_batch_size', default=128, type=int)
    parser.add_argument('--testdir', default="test/1", help="test result dir")
