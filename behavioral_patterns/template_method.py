from abc import ABC, abstractmethod


# Abstract class
class DocumentMiner(ABC):
    
    # template method
    def mine(self, filename): 
        file = self.open(filename)
        data = self.extract_data(file)
        result = self.analyzing_data(data)
        self.close(filename)
        return result
        
    @abstractmethod
    def open(self, filename: str):
        pass
    
    @abstractmethod
    def close(self, filename: str):
        pass
    
    def extract_data(self, file):
        print("Extracting data from file")
        return "Extracted data"
    
    def analyzing_data(self, data):
        print("Analyzing data")
        return "Analyzed data"


# Specific implementations
class PDFDocumentMiner(DocumentMiner):
    def open(self, filename: str):
        print(f"Opening PDF file: {filename}")
        return None
    
    def close(self, filename: str):
        print(f"Closing PDF file: {filename}")


class DocxDocumentMiner(DocumentMiner):
    def open(self, filename: str):
        print(f"Opening Docx file: {filename}")
        return None
    
    def close(self, filename: str):
        print(f"Closing Docx file: {filename}")


class CSVDocumentMiner(DocumentMiner):
    def open(self, filename: str):
        print(f"Opening CSV file: {filename}")
        return None
    
    def close(self, filename: str):
        print(f"Closing CSV file: {filename}")
        


if __name__ == "__main__":
    docx = DocxDocumentMiner()
    docx.mine("temp.docx")
    print('-------------\n')
    
    csv = CSVDocumentMiner()
    csv.mine("temp.csv")
    print('-------------\n')
    
    pdf = PDFDocumentMiner()
    pdf.mine("temp.pdf")