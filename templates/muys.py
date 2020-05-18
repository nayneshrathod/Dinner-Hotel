from javax.swing import JButton
from javax.swing import JFrame
import javax.swing


class Example(JFrame):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        panel = JPanel()
        self.getContentPane().add(panel)

        panel.setLayout(None)
        panel.setToolTipText("A Panel container")

        button = JButton("Button")
        button.setBounds(100, 60, 100, 30)
        button.setToolTipText("A button component")

        panel.add(button)

        self.setTitle("Tooltips")
        self.setSize(300, 200)
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLocationRelativeTo(None)
        self.setVisible(True)


if __name__ == '__main__':
    Example()