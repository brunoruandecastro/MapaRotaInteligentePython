U
    e�fa�  �                   @   s   G d d� d�Z dS )c                   @   s4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )�Pilhac                 C   s
   g | _ d S �N��cidades��self� r   �6C:\Users\bruno\Desktop\InteligenciaArtificial\pilha.py�__init__   s    zPilha.__init__c                 C   s   | j �|� d S r   )r   �append)r   �cidader   r   r   �empilhar   s    zPilha.empilharc                 C   s&   t �| �s| j�d�S td� d S d S )N�����u   A pilha já está vazia.)r   �
pilhaVaziar   �pop�printr   r   r   r   �desempilhar   s    
zPilha.desempilharc                 C   s
   | j d S )Nr   r   r   r   r   r   �getTopo   s    zPilha.getTopoc                 C   s   t | j�dkS )N�    )�lenr   r   r   r   r   r      s    zPilha.pilhaVaziaN)�__name__�
__module__�__qualname__r	   r   r   r   r   r   r   r   r   r      s
   	r   N)r   r   r   r   r   �<module>   �    