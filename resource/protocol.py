# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'protocol.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 625)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 623, 531))
        self.textBrowser.setMinimumSize(QtCore.QSize(623, 500))
        self.textBrowser.setMaximumSize(QtCore.QSize(603, 550))
        self.textBrowser.setStyleSheet("border:2 solid rgb(130, 130, 130);\n"
"background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 570, 75, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Microsoft 软件许可条款"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                最后更新日期：2018 年 6 月</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">微软软件许可条款</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">WINDOWS 操作系统</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">如果您居住（或业务主营地）在美国，请阅读第 11 节中具有约束力的仲裁条款和共同起诉弃权，它影响争议的解决方式。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">感谢您选择微软！</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">根据您获取 Windows 软件的方式，这是 (i) 您与设备制造商或使用您的设备分销软件的软件安装商之间的许可协议；或 (ii) 您与微软公司（或其位于您居住所在地或业务主营地的关联公司之一）之间的许可协议，前提是您的软件是从零售商处购买的。微软是微软或其关联公司之一所生产设备的设备制造商，如果您的软件是直接从微软购买的，则微软还是零售商。注意：如果您是批量许可客户，则您对该软件的使用应受批量许可协议的约束，而不是本协议的约束。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本协议介绍您的权利以及您使用 Windows 软件的前提条件。您应阅读完整协议，包括软件随附的任何补充许可条款以及所有链接条款，因为所有条款都很重要并一起构成适用于您的协议。您可通过将 (aka.ms/) 链接粘贴到浏览器窗口中来查看链接的条款。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">接受本协议或使用该软件，即表示您同意所有这些条款，并且同意按照第 3 节中介绍的隐私声明在软件的激活和使用期间传输特定信息。如果您不接受并遵守这些条款，则您可能不能使用该软件或其功能。您可以与设备制造商或安装商或零售商（如果您的软件是直接购买的）联系，了解相关退货规定并退还软件或设备以依据该规定获得退款。请务必遵守退货规定，其中的条款可能会要求您退还该软件以及安装有该软件的整个设备，才能获得退款（如有）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.    概述。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    适用性。本协议适用于您设备上预安装的、从零售商处购买的以及您安装的 Windows 软件、您用于接收软件的介质（如有）、软件附带的任何字体、图标、图像或声音文件，还有软件的任何微软更新、升级、补充程序或服务，除非它们附带有其他条款。本协议还适用于由 Microsoft 开发并提供诸如邮件、联系人、音乐和照片等功能的 Windows 应用程序，这些应用程序将包含在 Windows 中并作为其一部分。如果本协议包含有关设备上不可用功能或服务的条款，则这些条款不适用。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    附加条款。根据设备的功能、设备的配置方式和使用方式，您对某些功能、服务和应用程序的使用可能还适用其他微软和第三方条款。请务必阅读条款内容。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    一些 Windows 应用程序提供在线服务的访问点，或者依赖于在线服务，使用这些服务有时需要遵守单独的条款和隐私政策，例如 (aka.ms/msa) 上的微软服务协议。您可以通过查看服务使用条款或应用程序的设置（如果适用）来查看这些条款和政策。这些服务可能未在所有地区推出。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    微软、设备制造商或安装商可能会提供额外的应用程序，这些应用程序将受单独的许可条款和隐私政策的约束。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iii)    该软件包含依据 (aka.ms/adobeflash) 上的 Adobe Systems Incorporated 相关条款授予许可的 Adobe Flash Player。Adobe 和 Flash 是 Adobe Systems Incorporated 在美国和/或其他国家/地区的注册商标或商标。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iv)    该软件可能包含根据本协议或其各自的条款获得许可的第三方程序。您可在 (aka.ms/thirdpartynotices) 上查看适用于第三方程序的许可条款、通知和确认（如有）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(v)    当 Word、Excel、PowerPoint 和 OneNote 作为 Windows 随附的应用程序使用时，除非依据单独协议您具有商业使用之权利，否则您只能将其用于个人、非商业用途。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.    安装和使用权利。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    许可。该软件只授予使用许可，而非出售。根据本协议，我们授予您在您的设备（许可设备）上安装并运行该软件的一个实例的权利，一次供一人使用，但前提是您遵守本协议的所有条款。使用微软或授权来源的软件更新或升级非正版软件并不会使您原先的版本或更新/升级后的版本成为正版，并且在此情况下，您没有使用该软件的许可。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    设备。在本协议中，“设备”是指一种带有内部存储设备、能够运行软件的硬件系统（无论是物理硬件系统还是虚拟硬件系统）。硬件分区或刀片被视为设备。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c.    限制。设备制造商或安装商以及微软保留本协议中未明确授予的所有权利（如依据知识产权法享有的权利）。例如，本许可未授予您任何以下权利，并且您不得：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    单独使用或虚拟化软件的功能；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    发布、复制（除允许的备份复制之外）、出租、租赁或出借软件；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iii)    转让软件（除非本协议允许）；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iv)    绕过软件中的任何技术限制；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(v)    将软件用作服务器软件，用于商业托管服务，通过网络提供该软件以供多个用户同时使用，将软件安装在服务器上并允许用户远程访问，或将软件安装在设备上仅供远程用户使用；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(vi)    对该软件进行反向工程、反向编译或反汇编，或试图进行上述行为，除非且仅限于上述限制存在以下情形：(a) 适用法律允许；(b) 约束该软件可能包含的开源组件的使用的许可条款允许；或者 (c) 在该软件所包含或链接的 GNU 宽通用公共许可协议的许可下，进行必要的库变更调试；以及</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(vii)    当使用基于 Internet 的功能时，您不得以任何妨碍他人使用这些功能的方式使用它们，或试图在未经授权的情况下访问或使用任何服务、数据、帐户或网络。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d.    多使用方案。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    多个版本。如果在购买软件时为您提供了多个版本（例如 32 位和 64 位版本），您一次只能安装并激活其中一个版本。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    多个或组合连接。您用于多路复用或组合连接，或用于减少访问或使用软件的设备或用户的数量的硬件或软件不会减少您所需的许可数量。仅当您为所要使用的软件的每个实例拥有一个许可时，才能使用此类硬件或软件。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iii)    设备连接。您最多可允许 20 台其他设备访问安装在许可设备上的软件以使用下列软件功能：文件服务、打印服务、Internet 信息服务以及许可设备上的 Internet 连接共享和电话服务。您可以允许任意数量的设备访问许可设备上的该软件以在设备之间同步数据。然而，本节并不表示您有权在其中的任意其他设备上安装该软件，或使用该软件的主要功能（本节中列出的功能除外）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iv)    在虚拟环境中使用。本许可仅允许您在一台设备上安装一个软件实例，无论该设备是物理设备还是虚拟设备都是如此。如果要在多台虚拟设备上使用该软件，您必须为每个实例获取单独的许可。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(v)    远程访问。您可将实际使用许可设备的单一用户指定为许可用户，但频度不要超过每 90 天一次。许可用户可使用远程访问技术从其他设备访问许可设备。其他用户在不同的时间可使用远程访问技术从其他设备访问许可设备，但前提是在已单独获得运行此软件的相同版本或更高版本的许可的设备上。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(vi)    远程协助。您可以使用远程协助技术共享活动会话，而无需为该软件获取任何额外许可。远程协助允许一位用户直接连接到另一位用户的计算机，通常用于纠正问题。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e.    备份副本。您可以出于备份目的制作该软件的一个副本，也可按下文第 4 节所述使用该备份副本转让该软件（如果软件是作为独立软件购买的）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.    隐私；同意使用数据。您的隐私对于我们至关重要。部分软件功能会在您使用这些功能时发送或接收信息。其中的许多功能都可以在用户界面中关闭，或者您也可以选择不使用这些功能。接受本协议并使用该软件，即表示您同意微软按照微软隐私声明 (aka.ms/privacy) 以及与该软件功能关联的用户界面中的规定收集、使用和披露信息。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.    转让。如果您是在德国或 (aka.ms/transfer) 站点中所列的任何国家/地区购得本软件，本小节的条款概不适用，在这种情况下，将软件和软件使用权向第三方的任何转让都必须遵守适用的法律。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    预安装在设备上的软件。如果您购买了预安装在设备上的软件（并且如果您升级了预安装在设备上的软件），则只能将该软件的使用许可直接转让给具有许可设备的其他用户。转让必须包括该软件，并且如果与设备一起提供，则还必须包括含有产品密钥在内的正版 Windows 标签。在根据规定进行任何形式的转让之前，第三方必须同意在转让和使用该软件时遵守本协议。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    独立软件。如果您购买了作为独立软件的软件（并且如果您升级了作为独立软件购买的软件），则可将该软件转让给您拥有的其他设备。您也可以将该软件转让给由其他人所有的设备，前提是 (i) 您是该软件第一位获得许可的用户，并且 (ii) 新用户同意本协议的条款。您可以使用我们允许您制作的备份副本或者用来提供该软件的介质来转让该软件。每当您将该软件转让给一台新设备时，都必须将该软件从先前的设备上删除。您不得为了在设备之间共享许可而转让该软件。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.    授权软件和激活。只有在您经过了适当许可并且已经使用产品密钥或其他授权方式正确激活了软件的情况下，才授权您使用该软件。当您使用该软件连接到 Internet 时，该软件将自动与 Microsoft 或其关联公司联系，以进行激活并将其与某一特定设备相关联。您也可以通过 Internet 或电话手动激活该软件。在任一情况下，将发生特定信息的传输，并且可能收取 Internet、电话和 SMS 服务费用。在激活（或可能由设备的组件更改触发的重新激活）过程中，该软件可能确定软件的安装实例是否伪造、是否经过不当许可或是否包含未经授权的更改。如果激活失败，该软件将尝试通过将任何被篡改的 Microsoft 软件替换为正版 Microsoft 软件来进行自身修复。您还可能收到提醒，要求您获取软件的适当许可。激活成功并不能确认该软件为正版或经适当许可。您不得绕过或规避激活。请访问 (aka.ms/genuine)，以便确认您的软件是否为正版以及您是否已获得适当的许可。某些更新、支持和其他服务可能仅对正版微软软件的用户提供。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.    更新。该软件将定期检查系统和应用程序更新，并为您下载和安装这些更新。您只能获取微软或授权来源提供的更新，微软可能需要更新您的系统来为您提供这些更新。接受本协议，即表示您同意在无需任何额外通知的情况下接收这些类型的自动更新。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.    降级权利。如果您从制造商或安装商处购买的设备上预安装了 Windows 专业版且其被配置为以完整的功能模式运行，则您可使用 Windows 8.1 专业版或 Windows 7 专业版，但您仅可在 Microsoft 为该早期版本提供支持期间使用，相关规定请访问 (aka.ms/windowslifecycle)。使用早期版本时，您应遵守本协议。如果早期版本包含不同的组件，那么在使用这些组件时，您应遵守该早期版本附带的协议中所有适用于这些组件的条款。设备制造商、安装商或 Microsoft 均没有义务向您提供早期版本。您必须另行获得早期版本，这可能会产生一定的费用。您随时可以使用最初购买的版本替代早期版本。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8.    出口限制。您必须遵守适用于该软件的所有国内和国际出口法律和法规，其中包括对目的地、最终用户和最终用途的各种限制。有关出口限制的详细信息，请访问 (aka.ms/exporting)。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9.    保证、免责声明、补偿、损失和程序。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    有限保证。根据您获得微软软件的方式，微软、设备制造商或安装商保证，获得适当许可的软件会基本上按照软件附带的任何微软材料说明的方式运行。由您造成、或因您未遵守相关说明而引起、由超出微软、设备制造商或安装商合理控制范围的活动所造成的问题不在本有限保证范围之内。如果从微软该软件，或从设备制造商或安装商处购买该软件九十 (90) 天内，本有限保证自首位用户购买该软件起有效并持续一年时间。如果您在设备制造商的有限保证的九十 (90) 天期限内直接从微软获得更新或补充程序，微软会为这些更新或补充程序提供有限保证。如果从微软该软件，或从设备制造商或安装商处购买该软件九十 (90) 天内，您在这一年期限内从微软处收到的对该软件的补充程序、更新或更换也可以享受有限保证，但仅在该一年内剩余的有效期或 30 天内（以两者中时间较长者为准）享受有限保证。转让软件不会延长本有限保证。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    免责声明。微软、设备制造商和安装商均不提供任何其他明示保证、保障或条件。微软、设备制造商和安装商排除所有默示保证和条件，包括适销性、针对特定用途的适用性和不侵权的默示保证。如果您当地的法律不允许排除默示保证，则任何默示保证、保障或条件仅在有限保证期限内有效，且仅限于您当地的法律所允许的范围。如果您当地的法律要求更长的有限保证期限，则尽管有本协议，更长的期限将适用，但您只能获得本协议允许的补偿。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c.    有限补偿。如果微软、设备制造商和安装商违反其有限保证，则微软将自行选择：(i) 免费修复或更换该软件，或 (ii) 退还购买该软件（或预安装该软件的设备，由其自行选择）支付的金额（如有）并收回产品。设备制造商或安装商（或微软，如果您直接从微软购买）也可以修复或更换该软件的补充程序、更新和更换，或退还您支付的金额（如有）。这些是在违反保证的情况下您所能获得的唯一补偿。除了本有限保证提供的特定合法权利外，根据各州或者各个国家/地区的不同法律，您还可能享有其他权利。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d.    损害除了微软、设备制造商或安装商可能提供的任何修复、更换或退款之外，依据本有限保证、本协议的任何其他部分或任何理论，您不能因任何损害获得赔偿或其他补偿，包括利润损失、直接损害、后果性损害、特别损害、间接损害或附带损害。即使修复、更换或退款未完全补偿您的损失，如果微软、设备制造商或安装商知道或应该知道可能会出现损害，或者如果补偿未能达到其基本目的，本协议中的损害排除和补偿限制也同样适用。某些州和国家/地区不允许排除或限制附带损害赔偿、后果性损害赔偿或其他损害赔偿责任，因此这些限制或排除条款可能对您不适用。如果您当地的法律允许您因损害从微软、设备制造商或安装商处获得退款，则即使本协议不允许，您也可以获得，但您获得的退款不能超过您为该软件支付的金额（或者如果软件是免费获取的，则获得的金额上限为 50 美元）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e.    保证和退款程序。对于服务或退款，如果您从微软购买该软件，您必须提供购买凭证的副本并遵守微软的退回政策，或者，如果您从设备制造商或安装商处购买该软件，您需要遵守设备制造商或安装商的退回政策。如果您购买了独立软件，按照这些退回政策的要求，您可能需要卸载软件并将其归还到微软。如果您所购买了设备上的预装软件，退回政策可能需要您将软件连同安装软件的整个设备退回给微软；必须仍贴附包括产品密钥的“正版证书”标签（如果随设备一起提供）。请通过与您的设备一起提供的地址或免费电话与设备制造商或安装商联系，了解如何获得软件的保证服务。如果微软是您的设备制造商或者您的软件是从零售商处购买的，请通过以下方式联系微软：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    美国和加拿大。要了解保证服务或有关如何获得在美国或加拿大购买的软件的退款之信息，请通过以下方式联系微软：致电 (800) MICROSOFT；或发邮件至 Microsoft Customer Service and Support,One Microsoft Way, Redmond, WA 98052-6399, USA；或访问 (aka.ms/nareturns)。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    欧洲、中东和非洲。如果您是在欧洲、中东或非洲购买的软件，请联系 Microsoft Ireland Operations Limited, Customer Care Centre, Atrium Building Block B, Carmanhall Road, Sandyford Industrial Estate, Dublin 18, Ireland，或者联系为您所在国家/地区提供服务的微软关联公司，网址为 (aka.ms/msoffices)。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iii)    澳大利亚。如果您是在澳大利亚购买的软件，请通过以下方式联系微软以提出索赔：致电 13 20 58 或寄信至 Microsoft Pty Ltd, 1 Epping Road, North Ryde NSW 2113 Australia。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iv)    其他国家/地区。如果您是在其他国家/地区购买的软件，请联系为您所在国家/地区提供服务的微软关联公司，网址为 (aka.ms/msoffices)。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10.    支持。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    对于预安装在设备上的软件。有关该软件的一般支持选项，请向设备制造商或安装商咨询。可参见随软件提供的支持电话号码。对于直接从微软获取的更新和补充程序，微软可能会为获得适当许可的软件提供有限的支持服务，详见 (aka.ms/mssupport)。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    对于从零售商处购买的软件。微软为具有适当许可的软件提供有限支持服务，详见 (aka.ms/mssupport)。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11.    具有约束力的仲裁条款和共同起诉弃权（如果您的居住地或业务主营地在美国）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我们希望我们绝不会有争议，但如果发生了，您与我们同意尝试在六十 (60) 天内对争议进行非正式解决。如果我们无法解决，您与我们同意按照《联邦仲裁法》（以下简称“FAA”）接受美国仲裁协会（以下简称“AAA”）的有约束力的独立仲裁，而不是在法官或陪审团面前进行法律诉讼。中立的仲裁员将对争议进行裁决，并且仲裁员的裁决为最终裁决，但依据 FAA 享有有限审查权的除外。不允许共同起诉、共同范围的仲裁、检察长私人诉讼以及代理人提起的任何其他诉讼。如果未取得所有方的同意，也不得将单独的诉讼进行合并。“我们”和“我们的”包括微软、设备制造商和软件安装商。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    涉及除知识产权之外的所有内容的争议。术语“争议”具有尽可能广泛的含义。它包含您与设备制造商或安装商之间或者您与微软之间，依据包括合同、保证、侵权法、法令或法规在内的任何法理，就软件、软件价格或本协议而产生的任何索赔或争论，但不包括与您、您的许可方、我们或我们的许可方的知识产权的执行或有效性有关的争议。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    首先寄出争议通知。如果您有争议并且我们的客户服务代表无法解决，请通过美国邮政向设备制造商或安装商发送邮件，收件人：法律部。如果您的争议与 Microsoft 有关，请将争议通知寄给微软公司，收件人：CELA ARBITRATION, One Microsoft Way, Redmond, WA 98052-6399, USA。告诉我们您的姓名、地址、联系方式、问题所在以及您想要的结果。相关表格，请访问 (aka.ms/disputeform)。如果我们有与您有关的争议，同样也会这样做。六十 (60) 天后，如果争议未解决，您或我们可能会启动仲裁。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c.    小额索赔法院选择。如果您不愿意邮寄争议通知，并且您满足法院的要求，则可在您的居住县（或者您的业务主营地）或我们的主营地 — 美国华盛顿州金县（如果您的争议与 Microsoft 有关）的小额索赔法院起诉我们。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d.    仲裁程序。AAA 将依据其商事仲裁规则处理任何仲裁（如果您是个人并将该软件用于个人或家庭用途，或者争议的价值为 75,000 美元或以下金额，则无论您是否是个人或者无论您如何使用该软件，均将依据其消费者仲裁规则处理）。有关详细信息，请访问 (aka.ms/adr) 或致电 1-800-778-7879。若要启动仲裁，请将 (aka.ms/arbitration) 上提供的表格提交给 AAA；并将副本寄给设备制造商或安装商（如果您的争议与微软有关，则寄给微软）。在涉及 25,000 美元或以下金额的争议中，任何听证均将用电话传送，除非仲裁员找到合适的理由用在场听证取代。任何在场听证将在您的居住县（或业务主营地）或我们的业务主营地 - 华盛顿州的金县（如果您的争议与 Microsoft 有关）举行。具体由您选择。仲裁员可以像法院那样判给您个人相同的损害赔偿金。仲裁员只能判给您个人确认性或禁止令救济，以满足您的个人索赔。依据 AAA 规则，仲裁员在其自己管辖权地进行裁定，包括索赔的可仲裁性。但是法院拥有强制禁止集体性或代表性仲裁的唯一授权。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e.    仲裁费用和支付。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    涉及 75,000 美元或以下金额的争议。设备制造商或安装商（或微软，如果您的争议与微软有关）将及时补偿您的立案费并支付 AAA 和仲裁员的费用与支出。如果您拒绝我们在指定仲裁员之前作出的最后的书面庭外和解提议，您的争议最后将由仲裁员决定（称为“判决”），且如果仲裁员判给您超过此最后的书面提议的金额，设备制造商或安装商（或微软，如果您的争议与微软有关）将：(1) 支付判决金额或 1,000 美元两者间较大的金额；(2) 支付您合理的律师费（如有）；以及 (3) 补偿您的律师就在仲裁中调查、准备和进行索赔而合理产生的任何费用（包括专家证人费）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    涉及金额超过 75,000 美元的争议。AAA 规则将管辖立案费以及 AAA 和仲裁员的费用与支出。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">f.    必须在一 (1) 年内提出。您和我们必须在从争议最早可以提出的时间起的一 (1) 年内就任何索赔或争议向小额索赔法院起诉或提起仲裁（知识产权争议除外 - 请参阅第 11.a. 节）。否则，索赔或争议将被永久禁止。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">g.    可分割性。如果第 11 节的部分条款（具有约束力的仲裁条款和共同起诉弃权）被发现为非法的或不可执行的，其余部分将保持有效（在任何审批程序开始之前发出仲裁裁决）。例外是：发现部分违法性或不可执行性将导致集体性或有代表性的仲裁，第 11 节整体上不可执行。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">h.    与 AAA 规则冲突。如果本协议与 AAA 的商事仲裁规则或消费者仲裁规则相冲突，则以本协议为准。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">i.    微软作为一方或第三方受益人。如果微软是设备制造商或者您的软件是从零售商处购买的，则微软为本协议的一方。否则，微软不是本协议的一方，但是您和设备制造商或安装商的协议的第三方受益人，以通过非正式协商和仲裁解决争议。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12.    管辖法律。您所居住的州或国家/地区（若为企业，则为主要营业地）的法律管辖有关软件、软件价格或本协议的所有索赔和争议项目，包括违约索赔和根据消费者保护法、不正当竞争法、默示保证法、不当得利法以及侵权法提出的相关索赔，但不考虑冲突法原则。在美国，FAA 制约所有与仲裁相关的条款。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">13.    消费者权利，地区差异。本协议规定了某些合法权利。根据您所在州或国家/地区的法律规定，您可能享有其他权利（包括消费者权利）。您还可能享有与您的软件卖方相关的权利。如果您所在州或国家/地区的法律不允许本协议改变这些其他权利，则本协议将不改变这些其他权利。例如，如果您的软件是从下列地区之一购买的，或强制性的国家/地区法律适用，则下列条款适用于您：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    澳大利亚。提及的“有限保证”是指微软或设备制造商或安装商提供的明示保证。除了依照法律所拥有的其他权利和补偿（包括您依据澳大利亚消费者法中的消费者保障享有的权利和补偿），您还拥有此保证。此协议中的任何内容都不限制和更改那些权利和补偿。特别：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    在第 9 节标题为 “保证、免责声明、补偿、损失和程序” 的本地法律中排除有限保证、保障、损害和补偿，以及您的有限权利的期限的条款不适用于澳大利亚消费者法消费者保障和您在权利和补偿方面的权益；</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    有关支持和退款政策，请参考第 10 节，并受澳大利亚消费者法律约束。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iii)    澳大利亚消费者法消费者保障适用于第 14 d (ii) 节所述的软件评测和第 14 d (iv) 节所述的软件预览；和</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iv)    《澳大利亚消费者法》中的规定不会排除我们的商品附带的保障。在本节中， “产品” 指微软或设备制造商或安装商为其提供明示保证的软件。您有权就重大故障要求更换商品或退款，并就任何其他合理可预见的损失或损害获得补偿。您还有权在商品无法提供可接受的质量而存在的故障又不构成重大故障时要求维修或更换商品。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">有关更多澳大利亚消费者法中您的权利，请查阅“aka.ms/acl”中信息。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    加拿大。您可通过禁用 Internet 访问来停止接收设备更新。如果重新连接到 Internet，软件将继续检查并安装更新。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c.    欧盟。下文第 14.d(i) 节中的学术使用限制不适用于以下站点上所列的管辖权地：(aka.ms/academicuse) 。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d.    德国和奥地利。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    保证。获得适当许可的软件会基本上按照该软件附带的任何 Microsoft 材料说明的方式运行。但是，设备制造商或安装商和微软未提供任何与许可软件相关的合同保障。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    责任限制。如果出现基于产品责任法的故意行为、重大过失、索赔以及出现死亡或人身伤害的情况，设备制造商或安装商或微软将依据成文法负责。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">根据前面的声明，设备制造商或安装商或微软将仅对以下情况的轻微过失负责：设备制造商或安装商或微软违反此类实质性合同义务、未履行促使本协议正常执行的义务、危及本协议的目的的义务违反行为以及未能遵守一方可能一直相信要履行的义务（所谓的“基本义务”）。在其他轻微过失情况下，设备制造商或安装商或微软不对轻微过失负责。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">e.    其他地区。请访问 (aka.ms/variations) ，获取当前的地区差异列表。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">14.    附加声明。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a.    网络、数据和 Internet 使用。通过该软件访问的某些软件功能和服务可能要求您的设备访问 Internet。您的访问和使用（包括费用）可能受您的手机或 Internet 提供商协议条款的约束。某些软件功能可以帮助您更有效地访问 Internet，但软件的使用计算可能会与您的服务提供商的度量有所不同。您始终有责任 (i) 了解和遵守自己的计划和协议的条款，并且对 (ii) 因使用或访问网络（包括公共/开放的网络）引起的任何问题负责。只有在获得相关权限时，您才可以使用该软件来连接网络，并共享关于这些网络的访问信息。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">b.    H.264/AVC 和 MPEG-4 视频标准以及 VC-1 视频标准。该软件可能采用 H.264/MPEG-4 AVC 和/或 VC-1 解码技术。MPEG LA, L.L.C. 要求做出以下声明：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本产品受 AVC、VC-1 和 MPEG-4 PART 2 视频专利组合许可限制，仅供消费者个人使用和用于非商业用途，以便 (i) 对符合上述标准（以下简称“视频标准”）的视频进行编码和/或 (ii) 对消费者在从事个人和非商业活动过程中编码的 AVC、VC-1 和 MPEG-4 PART 2 视频和/或自获得提供此类视频许可的视频提供商处获得的此类视频进行解码。不授予或默示授予任何其他用途的许可。MPEG LA, L.L.C. 可能会提供额外信息。请访问 (AKA.MS/MPEGLA)。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c.    恶意软件防护。微软重视保护您的设备远离恶意软件。如果其他防护未安装或已过期，则该软件将启用恶意软件防护。为此，将禁用或可能必须删除其他反恶意软件。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d.    有限权利版本。如果您购买的软件版本标记为或另行设计为特定或有限使用，则您只能按规定使用软件。您不得将此类软件版本用于商业、非营利或营利活动。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(i)    学术。对于学术使用，您在购买时必须是教育机构的学生、人员或教员。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(ii)    产品评测。对于产品评测（或测试或演示）使用，您不得销售软件、在真实的操作环境下使用软件或在产品评测期之后使用软件。无论本协议中是否存在相反表述，评测软件均按“现状”提供，并且这些版本不适用任何明示或默示保证（包括有限保证）。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iii)    NFR。您不得销售标有“不得再销售”（“NFR”或“Not For Resale”）字样的软件。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(iv)    预览。您可以选择使用 Microsoft 可能提供的该软件的预览版、测试版、insider 版或其他预发布版本（以下简称“预览版”）。只要您遵守本协议的所有条款，您便可以使用预览版，但仅可在软件的到期日期之前使用。预览版仅作实验之用，可能与商业发行版本间存在着较大差异。无论本协议中是否存在相反表述，预览版均按“现状”提供，并且这些版本不适用任何明示或默示保证（包括有限保证）。在您的设备上安装预览版可能会影响您的设备保修或导致设备保修无效，并且可能会使您无法享受您的设备制造商或网络运营商提供的支持（视情况而定）。对于前述情形给您造成的任何损失，Microsoft 不承担任何责任。Microsoft 不为预览版提供支持服务。向 Microsoft 提供任何有关预览版的评论、建议或其他反馈（以下简称“提交内容”），即表示您授予 Microsoft 及其合作伙伴出于任何目的、以任何方式使用提交内容的权利。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15.    完整协议。本协议（以及由设备制造商、安装商或微软提供且您使用的任何软件补充程序、更新和服务附带的书面许可条款或其他条款），以及本协议中列出的 Web 链接中包含的条款，共同构成了该软件和任何此类补充程序、更新和服务的完整协议（除非由设备制造商、安装商或微软随此类补充程序、更新或服务提供其他条款）。您可在软件运行后通过转至 (aka.ms/useterms) 或转至软件中的“设置 - 系统 - 关于”查看本协议。也可以通过在浏览器地址栏中键入相应 URL 来查看本协议中的任何链接中的条款，且您同意如此行事。您同意，您会在使用该软件或服务之前阅读这些条款，包括任何链接的条款。您理解，使用软件和服务即表示您认可本协议及链接的条款。本协议中也包含一些提供信息的链接。以下是包含声明和具有约束力的条款的链接：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">·    Microsoft 隐私声明 (aka.ms/privacy)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">·    微软服务协议 (aka.ms/msa)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">·    Adobe Flash Player 许可条款 (aka.ms/adobeflash)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Form", "确定"))

