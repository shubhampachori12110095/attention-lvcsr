#!/usr/bin/env python
"""Learn to reverse the words in a text."""
import logging
import argparse
from lvsr.firsttry import main

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: %(name)s: %(levelname)s: %(message)s")
    parser = argparse.ArgumentParser(
        "Phoneme recognition on TIMIT",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "mode", choices=["train", "test"],
        help="The mode to run")
    parser.add_argument(
        "save_path", default="chain",
        help="The path to save the training process.")
    parser.add_argument(
        "--num-batches", default=20000, type=int,
        help="Train on this many batches.")
    parser.add_argument(
        "--from-dump", default=None,
        help="Path to the dump to be loaded")
    parser.add_argument(
        "--use-old", default=False, action="store_true",
        help="Use old model and log pickles")
    args = parser.parse_args()
    main(**vars(args))
