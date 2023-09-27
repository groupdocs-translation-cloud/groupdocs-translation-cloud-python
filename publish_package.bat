rmdir /S /Q build
rmdir /S /Q dist 
python setup.py bdist_wheel
python -m twine upload --repository pypi dist/* -u groupdocscloud -p GroupDocs123AbC