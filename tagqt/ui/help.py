from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QTextBrowser, QDialogButtonBox
)
from tagqt.ui.theme import Theme

class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        from PySide6.QtWidgets import QApplication
        self.setWindowIcon(QApplication.instance().windowIcon())
        self.setFixedWidth(500)
        self.setStyleSheet(Theme.current_stylesheet())
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Content
        self.browser = QTextBrowser()
        self.browser.setOpenExternalLinks(True)
        self.browser.setFixedWidth(460)
        layout.addWidget(self.browser)
        
        # Footer
        btn_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)

    def set_content(self, html):
        style = f"""
            <style>
                h3 {{ color: {Theme.ACCENT}; font-size: 13px;
                      font-weight: 600; margin-top: 12px; }}
                ul {{ margin: 4px 0; padding-left: 18px; }}
                li {{ margin: 3px 0; color: {Theme.TEXT}; }}
                b  {{ color: {Theme.TEXT}; }}
                code {{ background: {Theme.SURFACE1};
                        color: {Theme.MAUVE};
                        padding: 1px 4px;
                        border-radius: 3px; }}
                a  {{ color: {Theme.BLUE}; }}
            </style>
        """
        self.browser.setHtml(style + html)
        self.browser.document().setTextWidth(460)
        doc_height = self.browser.document().size().height()
        self.browser.setFixedHeight(int(doc_height) + 20)
        self.adjustSize()
        self.setFixedWidth(500)
