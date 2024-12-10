# yapf: disable

from setuptools import find_packages, setup

packages = find_packages()
requirements = [
    "torch",
    "torchvision",
    "pillow",
    # "fairseq>=0.10.2",
    "transformers",
    "sentence_transformers",
    "nltk>=3.5",
    "word2word",
    "wget",
    "joblib",
    "lxml",
    "g2p_en",
    "whoosh",
    "marisa-trie",
    "kss",
]

"""
pip install fairseq==0.10.0
pip install python-mecab-ko
pip install -e .
fairseq의 np.float -> np.float64로 수정
>>> /home/jinmang2/.conda/envs/jinmang2/lib/python3.11/site-packages/fairseq
>>> \bnp\.float\b(?!\d)
fairseq/dataclass/data_class.py 에서 mutable 부분 수정
>>> TrainingConfig, EvalLMConfig 부분 field(default_factory=...)로
pororo에서 from torchvision.models.vgg import model_urls 사용부분 주석처리
warning이 잔뜩 뜨더라!
- pretrained 인자 사용 x, weights 사용 (/home/jinmang2/.conda/envs/jinmang2/lib/python3.11/site-packages/torchvision/models/_utils.py:207)
- weights 파라미터에 잘못된 값 전달. enum class 사용해야함 (/home/jinmang2/.conda/envs/jinmang2/lib/python3.11/site-packages/torchvision/models/_utils.py:213)
- torch.load 사용시 `weights_only=False` 워닝 (/home/jinmang2/editable_packages/pororo/pororo/models/brainOCR/detection.py:80)
- copy_state_dict -> 보안 위험 (/home/jinmang2/editable_packages/pororo/pororo/models/brainOCR/detection.py:80)
"""

VERSION = {}  # type: ignore
with open("pororo/__version__.py", "r") as version_file:
    exec(version_file.read(), VERSION)

setup(
    name="pororo",
    version=VERSION["version"],
    description="Pororo: A Deep Learning based Multilingual Natural Language Processing Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    url="https://github.com/kakaobrain/pororo",
    author="kakaobrain Team SIGNALS",
    author_email="contact@kakaobrain.com",
    license="Apache-2.0",
    packages=find_packages(include=["pororo", "pororo.*"]),
    install_requires=requirements,
    python_requires=">=3.6.0",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    package_data={},
    include_package_data=True,
    dependency_links=[],
    zip_safe=False,
)
