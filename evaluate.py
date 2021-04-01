import sys
sys.path.append('PubTabNet/src')
from metric import TEDS


def load_html(path):
    return '\n'.join(open(path).readlines())


sample_gt = load_html('samples/sample_gt.html')
bs_pretty_gt = load_html('samples/bs_pretty_gt.html')
overspan_gt = load_html('samples/overspan_gt.html')


teds_evaluator = TEDS()


score = teds_evaluator.evaluate(sample_gt, sample_gt)
print('TEDS between sample_gt and sample_gt: %s' % score)


score = teds_evaluator.evaluate(bs_pretty_gt, sample_gt)
print('TEDS between sample_gt and bs_pretty_gt: %s' % score)


score = teds_evaluator.evaluate(overspan_gt, sample_gt)
print('TEDS between sample_gt and overspan_gt: %s' % score)
